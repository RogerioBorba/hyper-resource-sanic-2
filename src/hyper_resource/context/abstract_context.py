from typing import List

from src.hyper_resource.abstract_resource import AbstractResource
from src.hyper_resource.context.context_types import SQLALCHEMY_SCHEMA_ORG_TYPES, PYTHON_SCHEMA_ORG_TYPES
import copy
from environs import Env
from sqlalchemy.inspection import inspect

ACONTEXT_KEYWORK = "@context"
ATYPE_KEYWORK = "@type"
AID_KEYWORK = "@id"
env = Env()
env.read_env()
port = env.str("PORT", "8002")
host = env.str("HOST", "127.0.0.1")

PREFIX_HYPER_RESOURCE = "hr"
PREFIX_SCHEMA_ORG = "schema"

VOCABS_TEMPLATE = {
    f"{ACONTEXT_KEYWORK}": {
        f"{PREFIX_HYPER_RESOURCE}": f"http://{host}:{port}/core",
        f"{PREFIX_SCHEMA_ORG}": "http://schema.org/",
    }
}

class AbstractContext(object):
    def __init__(self, db_dialect, metadata_table, entity_class):
        self.db_dialect = db_dialect
        self.metadata_table = metadata_table
        self.entity_class = entity_class

    def get_basic_context(self):
        context = copy.deepcopy(VOCABS_TEMPLATE)
        context[ACONTEXT_KEYWORK].update(self.get_properties_term_definition_dict())
        # context.update(self.get_type_by_model_class())
        context.update(AbstractResource.MAP_MODEL_FOR_CONTEXT[self.entity_class].get_type_by_model_class())
        return context

    def get_projection_context(self, attributes: List[str]):
        context = copy.deepcopy(VOCABS_TEMPLATE)
        context[ACONTEXT_KEYWORK].pop(PREFIX_HYPER_RESOURCE)
        filtered_term_def_dict = dict()
        for term, definition in self.get_properties_term_definition_dict().items():
            if term in attributes:
                filtered_term_def_dict.update({term: definition})
        context[ACONTEXT_KEYWORK].update(filtered_term_def_dict)
        context.update(AbstractResource.MAP_MODEL_FOR_CONTEXT[self.entity_class].get_type_by_model_class())
        return context

    def get_foreign_key_context(self, fk_model):
        d = AbstractResource.MAP_MODEL_FOR_CONTEXT[fk_model].get_type_by_model_class()
        fk_context = {ATYPE_KEYWORK: AID_KEYWORK}
        fk_context[AID_KEYWORK] = d[ATYPE_KEYWORK]
        return fk_context

    def get_properties_term_definition_dict(self):
        fk_column_names = self.db_dialect.foreign_keys_names()
        term_definition_dict = {}
        for column in self.metadata_table.columns:
            if str(column.name) in fk_column_names:
                fk_col = self.db_dialect.foreign_key_column_by_name(column.name)
                fk_model = self.db_dialect.get_model_by_foreign_key(fk_col)
                term_definition_dict[str(column.name)] = self.get_foreign_key_context(fk_model)
            else:
                term_definition_dict[str(column.name)] = SQLALCHEMY_SCHEMA_ORG_TYPES[type(column.type)]
        return term_definition_dict

    @staticmethod
    def get_type_by_model_class():
        return {ATYPE_KEYWORK: PYTHON_SCHEMA_ORG_TYPES[object]}


class AbstractCollectionContext(AbstractContext):
    pass

class AbstractDetailContext(AbstractContext):
    pass