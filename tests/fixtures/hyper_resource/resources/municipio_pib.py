import sanic
import pandas as pd
from src.contexts.municipio_pib import MunicipioPibDetailContext
from src.hyper_resource.pandas_resource import PandasResource
from src.models.municipio_pib import MunicipioPib


class MunicipioPibResource(PandasResource):
    model_class = MunicipioPib
    context_class = MunicipioPibDetailContext

    def __init__(self, request, file_name_with_path: str):
        super().__init__(request)

    def entity_class(self):
        return MunicipioPib

    async def get_representation_path(self, path: str) -> str:
        pass

    async def get_representation(self) -> str:
        pass

class MunicipioPibCollectionResource(PandasResource):

    def entity_class(self):
        return MunicipioPib

    async def get_representation(self):
        try:
            records: list[dict] = await self. entity_class().records()
            return sanic.response.json(records)

        except SyntaxError as err:
            return sanic.response.json( err.message, err.code )

    async def get_representation_path(self, path: str):
        try:
            records: str = await self.entity_class().records()
            return sanic.response.text(path)
        except SyntaxError as err:
            return sanic.response.json(err.message, err.code)