
from src.hyper_resource.context.abstract_context import AbstractDetailContext
from src.hyper_resource.context.abstract_context import AbstractCollectionContext

class PessoaCollectionContext(AbstractCollectionContext):
    @staticmethod
    def get_type_by_model_class():
        return AbstractCollectionContext.get_type_by_model_class()

class PessoaDetailContext(AbstractDetailContext):
    @staticmethod
    def get_type_by_model_class():
        return AbstractDetailContext.get_type_by_model_class()
