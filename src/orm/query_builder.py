from typing import Optional, List

from sqlalchemy import select, Select
from src.orm.database import DialectDatabase
from src.orm.models import AlchemyBase
from src.url_interpreter.interpreter_error import PathError
from src.url_interpreter.interpreter_new import InterpreterNew


def first_word(path: str, separator: str = '/') -> str:
    """
    Returns the first word in path (str)
    Parameters
    path (str): is a substr from iri.  Ex.: filter/first_name/eq/John
    Return
     the first word in path (str)
    """
    parts: list [str] = path.split(separator)
    if len(parts):
        return path.split(separator)[0].strip().lower()
    raise PathError(message=f"path is not ok. Path: {path}", code=400)


class QueryBuilder:

    def __init__(self, dialect_db: DialectDatabase, entity_class: type, prefix_column: Optional[str] = None):
        self.columns: List = []
        self.wheres: List = []
        self.table_names: List = []
        self.group_by: Optional[str] = None
        self.order_by: Optional[str] = None
        self.offset_limit: Optional[str] = None
        self.has_group_by: bool = False
        self.has_count: bool = False
        self.has_sum: bool = False
        self.has_max: bool = False
        self.has_min: bool = False
        self.has_avg: bool = False
        self.has_geometry = False
        self.has_collect = False
        self._sql: Optional[str] = None
        self.geom_attribute_name: Optional[str] = None
        self.dialect_db = dialect_db
        self.entity_class = entity_class
        self.prefix_column: Optional[str] = prefix_column

    def column_name(self, attribute_name: str) -> str:
        return self.entity_class.column_name(attribute_name)

    def add_collect(self, express: str):
        self.add_column(express)
        self.has_collect = True

    def add_column(self, expr_column_name: str):
        self.columns.append(expr_column_name)

    def columns_size(self) -> int:
        return len(self.columns)

    def add_table_name(self, table_name: str):
        self.table_names.append(table_name)

    def add_where(self, expr_where: str):
        self.wheres.append(expr_where)

    def add_group_by(self, expr_group_by: str):
        column_names: List[str] = [self.column_name(att_name) for att_name in expr_group_by.split(',')]
        self.has_group_by = True
        self.group_by = ','.join(column_names)

    def add_order_by(self, order_by: str):
        self.order_by = order_by

    def add_offsetlimit(self, offset_limit_: str):
        self.offset_limit = offset_limit_

    def add_count(self, column_name: str = None):
        asterisk_or_column: str = column_name or '*'
        self.has_count = True
        self.add_column(f"count({asterisk_or_column})")

    def add_sum(self, sum_str: str):
        self.has_sum = True
        self.add_column(f"sum({self.column_name(sum_str)}) as sum_{sum_str}")

    def add_avg(self, avg_str: str):
        self.has_avg = True
        self.add_column(f"avg({self.column_name(avg_str)}) as avg_{avg_str}")

    def add_max(self, max_str: str):
        self.has_max = True
        self.add_column(f"max({self.column_name(max_str)}) as max_{max_str}")

    def add_min(self, min_str: str):
        self.has_min = True
        self.add_column(f"min({self.column_name(min_str)}) as min_{min_str}")

    def has_only_one_aggregate_math_function(self):
        return len(self.columns) == 1 and \
               (self.has_sum or self.has_count or self.has_avg or self.has_min or self.has_max) and \
               not self.has_group_by

    def exec_only_one_aggregate_math_function(self):
        if self.has_count:
            return self.count()
        if self.has_sum:
            return self.sum()

    def select_enum_columns(self) -> str:
        if len(self.columns) == 0:
            expr_column_name: str = self.dialect_db.column_names_alias(prefix_col_val=self.prefix_column)
            return f"select {expr_column_name} "
        return f"select {','.join(self.columns)} "

    def table_name(self) -> str:
        return f"from {','.join(self.table_names)} "

    def where(self) -> str:
        size: int = len(self.wheres)
        if size == 0:
            return ""
        elif size == 1:
            return f"where {self.wheres[0]} "
        return "where " + "and ".join([f"{where}" for where in self.wheres])

    def groupby(self) -> str:
        if self.group_by is None:
            return ""
        return f"group by {self.group_by} "

    def orderby(self)-> str:
        if self.order_by is None:
            return ""
        return f"{self.order_by} "

    def offsetlimit(self):
        if self.offset_limit is None:
            return ""
        return f"{self.offset_limit} "

    def query(self) -> str:
        if self._sql is None:
            self._sql = f"{self.select_enum_columns()}{self.table_name()}{self.where()}{self.groupby()}{self.orderby()}{self.offsetlimit()}"
        return self._sql

    def set_has_geometry(self, boolean: bool):
        if not self.has_geometry:
            self.has_geometry = boolean

    def set_geom_attribute_name(self,geom_attribute_name: str):
        self.geom_attribute_name = geom_attribute_name
        self.has_geometry = True

    async def count(self) -> int:
        return await self.dialect_db.count(where=self.where())

    async def sum(self) -> float:
        return await self.dialect_db.sum(self.columns[0], where=self.where())

    async def avg(self) -> float:
        return await self.dialect_db.avg(where=self.where())

    async def min(self) -> float:
        return await self.dialect_db.min(column_name=self.columns[0], where=self.where())

    async def fetch_all_as_geobuf(self):
        a_query: str = self.dialect_db.geobuf_query(self.query())
        rows = await self.dialect_db.fetch_all_by(a_query)
        if rows:
            row = rows[0]
            return row._mapping['st_asgeobuf']
        return None

    async def fetch_all_as_flatgeobuffers(self):
        a_query: str = self.dialect_db.flatgeobuf_query(self.query())
        rows = await self.dialect_db.fetch_all_by(a_query)
        if len(rows):
            row = rows[0]
            return row._mapping['st_asflatgeobuf']
        None

    def interpreter(self, path: str = ''):
        return InterpreterNew(path, self.entity_class, self.dialect_db)


class SAQueryBuilder:

    def __init__(self, dialect_db: DialectDatabase, entity_class: type[AlchemyBase], path: str, prefix_column: str | None = None):
        self.select: Select | None = None
        self.dialect_db = dialect_db
        self.entity_class = entity_class
        self.path = path
        self.paths = self.normalize_path_as_list("/*/")
        self.prefix_column: str | None = prefix_column

    def offset(self, path: str) -> None:
        """
        Add offset in the Select object
        path (str): is the offset/value1
        returns None
        """
        paths: list[str] = self.normalize_path_as_list(path, '/')
        offset: str = paths[0]
        if offset == '' or not paths[1].isnumeric():
            raise PathError("Error in path. the function offset must have one integer parameter", 400)

    def offsetlimit(self, path: str) -> None:
        """
        Add offsetlimit in the Select object
        path (str): is the offsetlimit/value1&value2
        returns None
        """
        paths: list[str] = self.normalize_path_as_list(path, '/')
        off_limit: list[str] = paths[1].split('&')
        if len(off_limit) != 2 or not off_limit[0].isnumeric() or off_limit[1].isnumeric():
            raise PathError("Error in path. the function offsetlimit must have two integer parameters", 400)
        self.select = self.select.offset(int(off_limit[0]))
        self.select = self.select.limit(int(off_limit[1]))

    def dict_function(self) -> dict[str, object]:
        """"""
        return {
            'collect': self.add_collect,
            'projection': self.add_projection,
            'count': self.add_count,
            'orderby': self.add_order,
            'filter': self.add_where,
            'offset': self.add_offset,
            'limit': self.add_limit,
            'offsetlimit': self.add_offsetlimit,
        }

    def dict_aggregate_function(self) -> dict:
        """"""
        return {
            'sum': self.add_sum,
            'avg': self.add_avg,
            'max': self.add_max,
            'min': self.add_min,
            'groupby': self.add_group_by,
        }

    def dict_all_function(self):
        """"""
        return {**self.dict_function(), **self.dict_aggregate_function()}


    def normalize_path_as_list(self, path: str, splitter: str = '/*/') -> list[str]:
        """Returns a list of path separated by splitter
        Parameters:
            path (str): a path from outside
            splitter (str): a separator string.
        Returns:
           A list(str).path.
           Ex.: unidade-federacao-a-list/nome,sigla,geom/*/filter/sigla/in/ES,RJ/*/orderby/sigla
           ['unidade-federacao-a-list/nome,sigla,geom','filter/sigla/in/ES,RJ', 'orderby/sigla']

        """
        path_local: str = path if path[0] != '/' else path[1:]
        paths: list[str] = path_local.split(splitter)
        return paths if paths[-1] != '' else paths[:-1]

    def column_name(self, attribute_name: str) -> str:
        return self.entity_class.column_name(attribute_name)

    def add_collect(self, express: str):
        self.add_column(express)
        self.has_collect = True

    def add_column(self, expr_column_name: str):
        self.columns.append(expr_column_name)

    def columns_size(self) -> int:
        return len(self.columns)

    def add_table_name(self, table_name: str):
        self.table_names.append(table_name)

    def add_where(self, expr_where: str):
        self.wheres.append(expr_where)

    def add_group_by(self, expr_group_by: str):
        column_names: List[str] = [self.column_name(att_name) for att_name in expr_group_by.split(',')]
        self.has_group_by = True
        self.group_by = ','.join(column_names)

    def add_order_by(self, order_by: str):
        self.order_by = order_by

    def add_offsetlimit(self, offset_limit_: str):
        self.offset_limit = offset_limit_

    def add_count(self, column_name: str = None):
        asterisk_or_column: str = column_name or '*'
        self.has_count = True
        self.add_column(f"count({asterisk_or_column})")

    def add_sum(self, sum_str: str):
        self.has_sum = True
        self.add_column(f"sum({self.column_name(sum_str)}) as sum_{sum_str}")

    def add_avg(self, avg_str: str):
        self.has_avg = True
        self.add_column(f"avg({self.column_name(avg_str)}) as avg_{avg_str}")

    def add_max(self, max_str: str):
        self.has_max = True
        self.add_column(f"max({self.column_name(max_str)}) as max_{max_str}")

    def add_min(self, min_str: str):
        self.has_min = True
        self.add_column(f"min({self.column_name(min_str)}) as min_{min_str}")

    def has_only_one_aggregate_math_function(self):
        return len(self.columns) == 1 and \
               (self.has_sum or self.has_count or self.has_avg or self.has_min or self.has_max) and \
               not self.has_group_by

    def exec_only_one_aggregate_math_function(self):
        if self.has_count:
            return self.count()
        if self.has_sum:
            return self.sum()

    def select_enum_columns(self) -> str:
        if len(self.columns) == 0:
            expr_column_name: str = self.dialect_db.column_names_alias(prefix_col_val=self.prefix_column)
            return f"select {expr_column_name} "
        return f"select {','.join(self.columns)} "

    def table_name(self) -> str:
        return f"from {','.join(self.table_names)} "

    def where(self) -> str:
        size: int = len(self.wheres)
        if size == 0:
            return ""
        elif size == 1:
            return f"where {self.wheres[0]} "
        return "where " + "and ".join([f"{where}" for where in self.wheres])

    def groupby(self) -> str:
        if self.group_by is None:
            return ""
        return f"group by {self.group_by} "

    def orderby(self)-> str:
        if self.order_by is None:
            return ""
        return f"{self.order_by} "

    def offsetlimit(self):
        if self.offset_limit is None:
            return ""
        return f"{self.offset_limit} "

    def query(self) -> str:
        if self._sql is None:
            self._sql = f"{self.select_enum_columns()}{self.table_name()}{self.where()}{self.groupby()}{self.orderby()}{self.offsetlimit()}"
        return self._sql

    def set_has_geometry(self, boolean: bool):
        if not self.has_geometry:
            self.has_geometry = boolean

    def set_geom_attribute_name(self,geom_attribute_name: str):
        self.geom_attribute_name = geom_attribute_name
        self.has_geometry = True

    async def count(self) -> int:
        return await self.dialect_db.count(where=self.where())

    async def sum(self) -> float:
        return await self.dialect_db.sum(self.columns[0], where=self.where())

    async def avg(self) -> float:
        return await self.dialect_db.avg(where=self.where())

    async def min(self) -> float:
        return await self.dialect_db.min(column_name=self.columns[0], where=self.where())

    async def fetch_all_as_geobuf(self):
        a_query: str = self.dialect_db.geobuf_query(self.query())
        rows = await self.dialect_db.fetch_all_by(a_query)
        if rows:
            row = rows[0]
            return row._mapping['st_asgeobuf']
        return None

    async def fetch_all_as_flatgeobuffers(self):
        a_query: str = self.dialect_db.flatgeobuf_query(self.query())
        rows = await self.dialect_db.fetch_all_by(a_query)
        if len(rows):
            row = rows[0]
            return row._mapping['st_asflatgeobuf']
        None

    def get_function_names(self) -> list[str]:
        """Returns a list of function names"""
        if self.function_names is None:
            collection_func: List[str] = super(FeatureCollectionResource, self).get_function_names()
            self.function_names = collection_func + self.dialect_DB().get_spatial_function_names() + list(self.dict_function().keys())
        return self.function_names

    def attribute_names(self) -> list[str]:
        """
        Returns a list of attribute names
        Returns list(str)

        """
        return self.entity_class.all_attributes_with_dereferenceable()

    def operation_name_in_path(self, path: str) -> str:
        operation_name_or_attribute_comma: str = first_word(path)
        if ',' in operation_name_or_attribute_comma or operation_name_or_attribute_comma in self.attribute_names():
            return 'projection'
        if operation_name_or_attribute_comma in self.get_function_names():
            return operation_name_or_attribute_comma
        msg = f"This {path} is incorrect"
        print(msg)
        raise PathError(msg, 400)

    def get_function_name_in_dict(self) -> str | None:
        """Returns the name of the correspondent function in the paths if exists, otherwise None.
        paths should like
        Returns
        function_name (str) or None """
        d = self.dict_all_function()
        for path in self.paths:
            func_name: str = self.operation_name_in_path(path)
            if func_name in d:
                return func_name
        return None
    def statement(self) -> Select:
        for path in self.paths:
            pass