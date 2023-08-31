import json

from sanic import  response
from typing import List, Dict, Optional, Any
from src.hyper_resource import feature_utils
from src.orm.models import AlchemyBase

MIME_TYPE_JSONLD = "application/ld+json"

from src.hyper_resource.basic_route import *


class AbstractResource:
    MAP_MODEL_FOR_CONTEXT = {}
    model_class = None

    def __init__(self, request):
        self.request = request
        self.dialect_db = None

    @classmethod
    def router_id(cls):
        return BasicRoute.router_id(cls.model_class)

    @classmethod
    def router_id_path(cls):
        return BasicRoute.router_id_path(cls.model_class)

    @classmethod
    def router_list(cls):
        return BasicRoute.router_list(cls.model_class)

    @classmethod
    def router_list_path(cls):
        return BasicRoute.router_list_path(cls.model_class)

    def dialect_DB(self):
        if self.dialect_db is None:
            self.dialect_db = self.request.app.ctx.dialect_db_class(self.request.app.ctx.db, self.metadata_table(), self.entity_class())
        return self.dialect_db

    def normalize_path_as_list(self, path: str, splitter) -> List[str]:
        paths: List[str] = path.split(splitter)
        return paths if paths[-1] != '' else paths[:-1]

    def accept_type(self) -> str:
        return self.request.headers['accept']

    def is_content_type_in_accept(self, accept_type: str):
        return accept_type in self.request.headers['accept']

    def protocol_host(self):
        return self.request.scheme + '://' + self.request.host

    def entity_class(self) -> type[AlchemyBase]:
        raise NotImplementedError("'entity_class' must be implemented in subclasses")

    def metadata_table(self):
        return self.entity_class().__table__

    def attribute_names(self):
        return self.entity_class().all_attributes_with_dereferenceable()
        
    def column_names(self) -> List[str]:
        return self.entity_class().column_names()

    def column_name(self, attribute_name: str) -> str:
        return self.entity_class().column_name(attribute_name)

    def fields_from_path_in_attribute_names(self, fields_from_path) -> bool:
        for att_name in fields_from_path:
            if att_name not in self.attribute_names():
                return False
        return True

    def fields_from_path_not_in_attribute_names(self, fields_from_path)-> bool :
        return not self.fields_from_path_in_attribute_names(fields_from_path)

    async def get_representation(self, id_or_key_value: Optional[Any] = None):
        raise NotImplementedError("'get_representation' must be implemented in subclasses")

    async def get_representation_given_path(self,  a_path : str):
        raise NotImplementedError("'get_representation' must be implemented in subclasses")

    async def head(self):
        return response.json("Method HEAD not implemented yet.", status=501)

    async def head_given_path(self, path : str):
        return response.json("Method HEAD not implemented yet.", status=501)

    async def options(self, *args, **kwargs):
        return response.json("Method OPTIONS not implemented yet.", status=501)
    
    #'/string/<parameters:path>'
    async def options_given_path(self, path):
        return response.json("Method OPTIONS not implemented yet.", status=501)

    async def post(self):
        return response.json("Method POST not implemented yet.", status=501)

    async def patch(self, id):
        return response.json("Method PATCH not implemented yet.", status=501)

    async def put(self, id):
        return response.json("Method PUT not implemented yet.", status=501)

    async def delete(self, id):
        return response.json("Method DELETE not implemented yet.", status=501)

    def get_function_names(self) -> list[str]:
        """
        Returns a list of function name that a resource should respond to.

        Return
            function names (list[str])
        """
        raise NotImplementedError("'get_function_names' must be implemented in subclasses")
    def validate_attribute_names(self, attribute_names: List[str]) -> bool:
        s1 = set(self.dialect_DB().attribute_names())
        s2 = set(attribute_names)
        set_final = s2.difference(s1)
        if len(set_final) > 0:
            raise NameError(f"The attribute list was not found: {set_final.__str__()}")
        return True

    def validate_data(self, attribute_value: dict):
        attribute_names = list(attribute_value.keys())
        self.validate_attribute_names(attribute_names)

    def set_html_variables(self, html_content:str)-> str:
        return feature_utils.set_html_variables(
            html_content, self.metadata_table().name,
            json.dumps(
                self.context_class(
                    self.dialect_DB(),
                    self.metadata_table(),
                    self.entity_class()
                ).get_basic_context(),
                indent=2
            )
        )