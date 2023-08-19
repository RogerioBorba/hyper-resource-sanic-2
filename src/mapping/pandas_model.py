import json

import numpy as np
import pandas as pd
from pandas import DataFrame


class PandasModel:
    df = None
    @classmethod
    def file_name_with_path(cls) -> str:
        """Returns string that is the name of the file with the path in Subclasses
            Returns file name with path (str)
        """
        raise NotImplementedError("The class method file_name_with_path must be implemented in subclasses")

    @classmethod
    async def load_data_frame(cls) -> DataFrame:
        """Returns a dataFrame (DataFrame) - Load data into DataFrame(df) from file (file_name_with_path)

            Parameters:

            Returns:
                DataFrame
        """
        encoding: str = 'utf8'
        if cls.file_name_with_path().endswith('.csv'):
            return pd.read_csv(cls.file_name_with_path(), encoding=encoding)
        elif cls.file_name_with_path().endswith('.xls') or cls.file_name_with_path().endswith('.xlsx'):
            return pd.read_excel(cls.file_name_with_path(), encoding=encoding)
        else:
            raise Exception(f"Sorry, problems to load file {cls.file_name_with_path()}")

    @classmethod
    async def get_df(cls) -> DataFrame:
        """Returns a dataFrame (DataFrame)

            Returns:
                DataFrame
        """
        if cls.df is None:
            local_df: DataFrame = await cls.load_data_frame()
            cls.df = local_df.replace(np.nan, None)
        return cls.df

    @classmethod
    async def records(cls) -> list[dict]:
        result: DataFrame = await cls.get_df()
        return result.to_dict(orient='records')

    @classmethod
    async def records_as_json(cls) -> str:
        result: list[dict] = await cls.records()
        return json.dumps(result)
