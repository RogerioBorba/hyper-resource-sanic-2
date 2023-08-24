from pandas import DataFrame

from src.mapping.pandas_model import PandasModel


class MunicipioPib(PandasModel):
    #df: DataFrame | None = None

    @classmethod
    def file_name_with_path(cls) -> str:
        """Returns str that is the name of the file with the path
            Returns file name with path (str
        """
        return 'C://dados//IBGE//pib_municipios//PIB-2010-2020.csv'


class Munic(PandasModel):
    #df: DataFrame | None = None

    @classmethod
    def file_name_with_path(cls) -> str:
        """Returns str that is the name of the file with the path
            Returns file name with path (str
        """
        return 'C://dados//IBGE//pib_municipios//PIB-2002-2009.csv'
