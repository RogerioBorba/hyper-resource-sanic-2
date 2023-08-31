from typing import Optional, List

from sqlalchemy import Select, text, Column, case
from sqlalchemy.orm import InstrumentedAttribute

from src.hyper_resource.abstract_resource import AbstractResource
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
    parts: list[str] = path.split(separator)
    if len(parts):
        return path.split(separator)[0].strip().lower()
    raise PathError(message=f"path is not ok. Path: {path}", code=400)


def normalize_path_as_list(path: str, splitter: str = '/*/') -> list[str]:
    """Returns a list of path separated by splitter
    Parameters:
        path (str): a path from outside
        splitter (str): a separator string.
    Returns:
       A list(str) of path.
       Ex.: unidade-federacao-a-list/nome,sigla,geom/*/filter/sigla/in/ES,RJ/*/orderby/sigla
       ['unidade-federacao-a-list/nome,sigla,geom','filter/sigla/in/ES,RJ', 'orderby/sigla']

    """
    print("---------------------------------------------------------------------")
    print(path)
    if len(path) == 0:
        return path
    path_local: str = path if path[0] != '/' else path[1:]
    paths: list[str] = path_local.split(splitter)
    return paths if paths[-1] != '' else paths[:-1]


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


class SASQLBuilder:

    def __init__(self, resource: AbstractResource, path: str, prefix_column: str | None = None, delimiter: str = '/*/'):
        self.select: Select | None = None
        self.resource = resource
        self.path = path
        self.paths = normalize_path_as_list(path=path, splitter=delimiter)
        self.prefix_column: str | None = prefix_column
        self.function_names = None
        self.projection: list[str] = self.attribute_names()

    def dict_function(self) -> dict[str, object]:
        """"""
        return {
            'collect': self.add_collect,
            'projection': self.add_projection,
            'count': self.add_count,
            'orderby': self.add_order_by,
            'filter': self.add_where,
            'offset': self.add_offset,
            'limit': self.add_limit,
            'offsetlimit': self.add_offset_limit,
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

    def interpreter(self, path: str) -> InterpreterNew:
        """
        Returns an instance of InterpreterNew to generate sql expression

        Parameters
            path(str) - path to be interpreted and converted to sql expression

        Returns
                interpreter(InterpreterNew)
        """
        dialect_db: DialectDatabase = self.resource.dialect_DB()
        entity_class: type[AlchemyBase] = self.resource.entity_class()
        return InterpreterNew(an_expression=path, model_class=entity_class, dialect_db=dialect_db)

    def get_select(self) -> Select:
        if self.select is None:
            self.select = Select(*self.columns_alias()).select_from(self.resource.metadata_table())
        return self.select

    async def add_where(self, path: str) -> None:
        """translate path in a sql expression (predicate) to add in Select object.
           Example: path = filter/valor/gt/100 will render an expression valor > 100 to be appended in Select object

            Paramaters
                path (str) - is a string containing an external expression, such as filter/valor/gt/100, i.e,
                operation name and rest of the string.


            Returns
                None
        """
        path_without_operation_name: str = "/".join(path.split("/")[1:])
        expr: str = await self.interpreter(path_without_operation_name).translate_lookup()
        self.select = self.get_select().where(text(expr))

    def add_collect(self, path: str) -> None:
        pass

    def all_external_attributes_exists(self, ext_attr_names: set[str]) -> bool:
        """Returns True if all external attribute in the ext_attr_names exists as attribute name in the model class
        Parameters
            ext_attr_names (set[str]) - is a set of external attribute names coming from path
        Returns a (bool)
        """
        set_attr_names = set(self.attribute_names())
        return set_attr_names.union(ext_attr_names) == set_attr_names

    async def add_projection(self, path: str) -> None:
        ext_attr_names: set[str] = {att_name.strip() for att_name in path.lower().split(',')}
        if self.all_external_attributes_exists(ext_attr_names):
            self.projection = list(ext_attr_names)
        else:
            dif: set[str] = ext_attr_names.difference(self.attribute_names())
            raise PathError(f"Error in {dif}", code=400)

    def add_order_by(self, path: str) -> None:
        pass

    def add_count(self, path: str) -> None:
        pass

    def add_group_by(self, path: str) -> None:
        pass

    def add_offset(self, path: str) -> None:
        pass

    def add_limit(self, path: str) -> None:
        pass

    def add_offset_limit(self, path: str) -> None:
        pass

    def add_sum(self, path: str) -> None:
        pass

    def add_avg(self, path: str) -> None:
        pass

    def add_max(self, path: str) -> None:
        pass

    def add_min(self, path: str) -> None:
        pass

    def dialect_db(self) -> DialectDatabase:
        return self.resource.dialect_db

    async def fetch_all_as_geobuf(self):
        a_query: str = self.dialect_db().geobuf_query(self.query())
        rows = await self.dialect_db().fetch_all_by(a_query)
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

    async def execute_operation(self,  path: str) -> None:
        """Executes the operation in path to add statement in Select object

        Paramaters
            path (str) - is a string containing an expression, i.e, operation name and rest of the string.
            Example: filter/valor/gt/100, where filter is the operation name to be executed to be appended in Select object

        Returns
            None
        """
        operation_name: str = self.operation_name_in_path(path)
        if operation_name not in self.dict_all_function().keys():
            msg: str = f"Error in path. This {operation_name} does not exists"
            raise PathError(msg, 400)
        return await self.dict_all_function()[operation_name](*[path])

    def get_function_names(self) -> list[str]:
        """Returns a list of function names. Each type of resource has different functions
            Returns
                list(str) - list function names
        """
        if self.function_names is None:
            self.function_names = self.resource.get_function_names()
        return self.function_names

    def entity_class(self) -> type[AlchemyBase]:
        return self.resource.entity_class()

    def attribute_names(self) -> list[str]:
        """
        Returns a list of attribute names
        Returns list(str)

        """
        return [name for name, attrib in self.entity_class().attributes_with_dereferenceable()]


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

    async def select_statement(self) -> Select:
        """Returns a Select object from paths
        Returns
        (Select)"""

        for path in self.paths:
            await self.execute_operation(path)
        self.select = self.get_select()
        return self.get_select()

    def alias_column(self, inst_attr: InstrumentedAttribute) -> object:
        if self.entity_class().is_relationship_fk_attribute(inst_attr) and self.prefix_column is not None:
            col = self.entity_class().column(inst_attr)
            model_class = self.entity_class().class_given_relationship_fk(inst_attr)
            prefix_model: str = f"{self.prefix_column}{model_class.router_list()}/"
            a_case = case((inst_attr is not None, col._rconcat(prefix_model)), else_=None).label(f"{self.entity_class().attribute_name_given(inst_attr)}")
            return a_case
            #return f"CASE WHEN {col_name} is not null THEN '{self.prefix_col}{model_class.router_list()}/' || {col_name} ELSE null  END AS {self.entity_class.attribute_name_given(inst_attr)}"
        elif self.entity_class().is_primary_key(inst_attr):
            pref = f'{self.prefix_column}{self.entity_class().router_list()}/' if self.prefix_column is not None else ''
            col = self.entity_class().column(inst_attr)
            attr_name = self.entity_class().attribute_name_given(inst_attr)
            return col._rconcat(pref).label(attr_name) if self.prefix_column is not None else col.label(attr_name)
        elif self.entity_class().is_relationship_attribute(inst_attr):
            return None
        else:
            col = self.entity_class().column(inst_attr)
            attr_name = self.entity_class().attribute_name_given(inst_attr)
            return col.label(attr_name)
        #c = case((Gasto.valor > 1000, Gasto.valor * 20), else_=Gasto.valor)

    def columns_alias(self) -> list:
        attr_names = self.projection
        attributes = [self.entity_class().__dict__[name] for name in attr_names if name in self.entity_class().__dict__.keys()]
        list_col = []
        for att in attributes:
            col: Column | None = self.alias_column(att)
            if col is not None:
                list_col.append(col)
        return list_col
