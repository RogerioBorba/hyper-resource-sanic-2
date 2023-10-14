import time
from asyncpg import UniqueViolationError, DataError
import sanic
from typing import  List
from src.hyper_resource.context.abstract_context import AbstractCollectionContext
from .abstract_collection_resource import AbstractCollectionResource
from ..orm.dictionary_actions_abstract_collection import dic_abstract_collection_action

class CollectionResource(AbstractCollectionResource):
    def __init__(self, request: sanic.request.Request, context_class: type, function_names: list[str]):
        super().__init__(request, context_class, function_names)
        self.context_class = AbstractCollectionContext

    def get_function_names(self) -> List[str]:
        if self.function_names is None:
            self.function_names = list(dic_abstract_collection_action.keys())
        return self.function_names


