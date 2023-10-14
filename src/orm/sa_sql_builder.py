# -*- coding: latin-1 -*-
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.orm import InstrumentedAttribute
from sqlalchemy.sql.functions import _FunctionGenerator
from src.orm.query_builder_util import normalize_path_as_list, first_word, HYPER_OPERATION_NAMES, \
    path_without_last_slash
from src.orm.query_builder_util import comma_list_str_as_list, path_as_list
from src.orm.query_builder_util import AVG, COLLECT, COUNT, FILTER, LIMIT, MAX, MIN, OFFSET, SUM
from src.orm.query_builder_util import GROUPBY, OFFSETLIMIT, ORDERBY, PROJECTION
from sqlalchemy import Select, text, literal_column, desc, asc, func, Column, Engine, Table, case
from src.orm.database import DialectDatabase
from src.orm.models import AlchemyBase
from src.hyper_resource.abstract_resource import AbstractResource
from src.url_interpreter.interpreter_error import PathError
from src.url_interpreter.interpreter_new import InterpreterNew


class SASQLBuilder:
    # Select is composed of: projection, from, where, group by, having, order by
    def __init__(self, resource: AbstractResource, path: str, prefix_column: str | None = None, delimiter: str = '/*/'):
        self.select: Select | None = None
        self.resource: AbstractResource = resource
        self.path: str = path
        self.paths: list[str] = []
        self.prefix_column: str | None = prefix_column
        self.function_names: list[str] | None = None
        self.projection: list = []
        self.has_count = False
        self.has_sum: bool = False
        self.has_max: bool = False
        self.has_min: bool = False
        self.has_avg: bool = False
        self.has_projection: bool = False
        self.has_collect: bool = False
        self.has_filter: bool = False
        self.has_offset: bool = False
        self.has_limit: bool = False
        self.has_offsetlimit: bool = False
        self.has_groupby: bool = False
        self.has_having: bool = False
        self.has_orderby: bool = False
        self.initialize_attributes(path, delimiter)

    def initialize_attributes(self, path: str, delimiter: str = '/*/'):
        """
        Initialize variables to reflect the expressions that are in the paths
        Return None:
        """
        self.paths = normalize_path_as_list(path, delimiter)
        for a_path in self.paths:
            operation_name = first_word(a_path)
            if operation_name in HYPER_OPERATION_NAMES:
                setattr(self, f"has_{operation_name}", True)

    def projection_is_empty(self) -> bool:
        """
        Returns true if projection is empty
        Returns (bool)

        """
        return len(self.projection) == 0

    def set_true_operation_in_path(self, operation_name) -> None:
        """Sets true if operation is in path
         Parameters
         operation_name (str) - operationa name in the path. Ex.: max/value
         Returns
           None
         """

    def dict_operation(self) -> dict[str, object]:
        """"""
        return {
            COLLECT: self.add_collect,
            PROJECTION: self.add_projection,
            COUNT: self.add_count,
            ORDERBY: self.add_order_by,
            FILTER: self.add_where,
            OFFSET: self.add_offset,
            LIMIT: self.add_limit,
            OFFSETLIMIT: self.add_offset_limit,
        }

    def dict_aggregate_operation(self) -> dict:
        """"""
        return {
            SUM: self.add_sum,
            AVG: self.add_avg,
            MAX: self.add_max,
            MIN: self.add_min,
            GROUPBY: self.add_group_by,
        }

    def dict_all_operation(self):
        """"""
        return {**self.dict_operation(), **self.dict_aggregate_operation()}

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


    def get_projection(self) -> list:
        """
        Returns the projection in SqlAlchemy contending object of type columns and others in list
        Returns (list)
        """
        if self.projection_is_empty():
            self.projection = self.columns_alias()
        return self.projection

    def get_select(self) -> Select:
        if self.select is None:
            self.select = Select(*self.get_projection()).select_from(self.resource.metadata_table())
        return self.select

    def set_select(self, select_obj: Select) -> None:
        self.select = select_obj

    def len_columns(self) -> int:
        return len(self.get_select().selected_columns)

    def has_only_one_aggregate_math_function(self) -> bool:
        """
        Returns True if select has only one aggregate function and not have group by
        Returns bool
        """
        return self.len_columns() == 1 and (self.has_sum or self.has_count or self.has_avg or self.has_min or
                                            self.has_max) and not self.has_group_by()

    def all_external_attributes_exists(self, ext_attr_names: set[str]) -> bool:
        """Returns True if all external attribute in the ext_attr_names exists as attribute name in the model class
        Parameters
            ext_attr_names (set[str]) - is a set of external attribute names coming from path
        Returns a (bool)
        """
        set_attr_names = set(self.attribute_names())
        return set_attr_names.union(ext_attr_names) == set_attr_names

    def check_all_external_attributes(self, ext_attr_names: set[str]) -> set[str]:
        """Returns a set of ext_attr_names. If some external attribute in the ext_attr_names does not exist
         as attribute name in the model class, an exception (PathError) will be raised
                Parameters
                    ext_attr_names (set[str]) - is a set of external attribute names coming from path
                Returns a (set[str])
        """
        if not self.all_external_attributes_exists(ext_attr_names):
            set_result: set[str] = set(ext_attr_names) - set(self.attribute_names())
            if len(set_result) == 0:
                return set_result
            if len(set_result) == 1:
                raise PathError(message=f"This {set_result.pop()} attribute does not exists", code=400)
            raise PathError(message=f"These attributes {set_result} do not exist", code=400)

    async def add_where(self, path: str) -> None:
        """translate path in a sql expression (predicate) to add in Select object.
           Example: path = filter/valor/gt/100 will render an expression valor > 100 to be appended in Select object

            Paramaters
                path (str) - is a string containing an external expression, such as filter/valor/gt/100, i.e,
                operation name and rest of the string.


            Returns
                None
        """
        path_without_operation_name: str = "/".join(path.split('/')[1:])
        expr: str = await self.interpreter(path_without_operation_name).translate_lookup()
        self.select = self.get_select().where(text(expr))

    async def add_collect(self, path: str) -> None:
        self.has_collect = True
        path_as_lst: list[str] = path_as_list(path)
        if len(path_as_lst) < 3:
            raise PathError(message=f'Collect path, {path}, is incorrect', code=400)
        attribute_name: str = path_as_lst[1].strip().lower()
        if not self.entity_class().has_attribute(attribute_name):
            raise PathError(message=f'Attribute {attribute_name} does not exist', code=400)
        expr: str = await self.interpreter(path).translate_to_collect(path, protocol_host=self.resource.protocol_host())
        label: str = f'{path_as_lst[1]}_{path_as_lst[-1]}'
        literal_col = literal_column(expr).label(label)
        self.projection.append(literal_col)

    async def add_projection(self, path: str) -> None:
        projection: str = 'projection'
        self.has_projection = True
        a_path: str = path if path.startswith(projection) else f"projection/{path}"
        attrib_names_str: str = path_as_list(a_path)[1]
        ext_attr_names: set[str] = {att_name.strip().lower() for att_name in attrib_names_str.split(',')}
        if self.all_external_attributes_exists(ext_attr_names):
            self.projection = self.columns_alias(list(ext_attr_names))
        else:
            self.has_projection = False
            dif: set[str] = ext_attr_names.difference(self.attribute_names())
            raise PathError(f"Error in path {dif}", code=400)

    async def add_order_by(self, path: str) -> None:
        local_path_str: str = path.lower()
        local_path: list[str] = path_as_list(local_path_str)  #path = orderby/valor&desc/
        attribute_order_str: str = local_path[1] #valor&desc
        attribute_order_list: list[str] = attribute_order_str.split('&')
        attribute_names: list[str] = attribute_order_list[0].split(',')
        if not self.all_external_attributes_exists(attribute_names):
            res = set(attribute_names) - set(self.attribute_names())
            if len(res) == 1:
                raise PathError(f"The attribute {list(res).pop()} does not exists", 400)
            raise PathError(f"These attributes {','.join(list(res))} do not exist", 400)

        if len(attribute_order_list) == 1: #valor
            return self.set_select(self.get_select().order_by(*attribute_names))
        if len(attribute_order_list) == 2: #valor&desc
            attribute_orders: list[str] = attribute_order_list[1].split(',')
            orders: list = []
            if len(attribute_names) == len(attribute_orders):
                for idx, att_name in enumerate(attribute_names):
                    attrib_order = desc(att_name) if attribute_orders[idx] == 'desc' else asc(att_name)
                    orders.append(attrib_order)
                self.set_select(self.get_select().order_by(*orders))
            else:
                order: str = attribute_orders[0]
                for att_name in attribute_names:
                    attrib_order = desc(att_name) if order == 'desc' else asc(att_name)
                    orders.append(attrib_order)
                self.set_select(self.get_select().order_by(*orders))

    async def add_count(self, path: str) -> None:
        self.has_count = True
        path_list: list[str] = path_as_list(path)
        a_func = func.count(path_list[1]) if len(path_list) >= 2 else func.count()
        self.projection.append(a_func)

    async def add_group_by(self, path: str) -> None:
        path_list: list[str] = path_as_list(path) #groupby/tipo_gasto/
        if self.projection_is_empty():
            raise PathError(message=f"Error in path {path_list}. Group by attribute must be in projection.", code=400)
        if len(path_list) != 2:
            raise PathError(message=f"Error in path {path_list}", code=400)
        group_ats: list[str] = comma_list_str_as_list(path_list[1]) #groupby/tipo_gasto/
        self.check_all_external_attributes(set(group_ats))
        self.has_groupby = True
        col_names: list[str] = self.entity_class().column_names_given(group_ats)
        select: Select = self.get_select().group_by(*col_names)
        self.set_select(select)

    async def add_offset(self, path: str) -> None:
        try:
            self.has_offset = True
            offset: int = int(path.split("/")[1])
            select: Select = self.get_select().offset(offset)
            self.set_select(select)
        except ValueError:
            raise PathError(message=f"path must have 1 integer. Path: {path}", code=400)
        except Exception:
            raise PathError(message=f"path is not ok. Path: {path}", code=400)

    async def add_limit(self, path: str) -> None:
        try:
            self.has_limit = True
            limit = int(path.split("/")[1])
            select: Select = self.get_select().limit(limit)
            self.set_select(select)
        except ValueError:
            raise PathError(message=f"path must have 1 integer. Path: {path}", code=400)
        except Exception:
            raise PathError(message=f"path is not ok. Path: {path}", code=400)

    async def add_offset_limit(self, path: str) -> None:
        try:
            self.has_offsetlimit = True
            offset, limit = path.split("/")[1].split('&')
            select: Select = self.get_select().slice(int(offset), int(limit))
            self.set_select(select)

        except ValueError:
            raise PathError(message=f"path must have 2 integers separated by &. Path: {path}", code=400)
        except Exception:
            raise PathError(message=f"path is not ok. Path: {path}", code=400)

    async def add_aggragate_function(self, path: str, funct: _FunctionGenerator):
        a_path = path.split("/")
        attribute_name: str = a_path[1]
        col: Column = self.entity_class().column_given(attribute_name)
        a_func = funct(col)
        self.projection.append(a_func)

    async def add_sum(self, path: str) -> None:
        self.has_sum = True
        return await self.add_aggragate_function(path, func.sum)

    async def add_avg(self, path: str) -> None:
        self.has_avg = True
        return await self.add_aggragate_function(path, func.avg)

    async def add_max(self, path: str) -> None:
        self.has_max = True
        return await self.add_aggragate_function(path, func.max)

    async def add_min(self, path: str) -> None:
        self.has_min = True
        return await self.add_aggragate_function(path, func.min)

    def has_group_by(self) -> bool:
        return len(self.get_select()._group_by_clauses) > 0

    def dialect_db(self) -> DialectDatabase:
        return self.resource.dialect_DB()

    def db(self) -> AsyncEngine | Engine:
        return self.dialect_db().db

    async def fetch_one(self):
        async with self.db().connect() as conn:
            result = await conn.execute(self.get_select())
            return result.one_or_none()

    async def fetch_all(self):
        async with self.db().connect() as conn:
            result = await conn.execute(self.get_select())
            rows = result.fetchall()
            return rows

    async def count(self) -> int:
        """
        Returns the amount of resource

        """
        qtd = await self.fetch_one()
        return qtd if qtd is not None else 0

    async def execute_operation(self,  path: str) -> None:
        """Executes the operation in path to add statement in Select object

        Paramaters
            path (str) - is a string containing an expression, i.e, operation name and rest of the string.
            Example: filter/valor/gt/100,
            where filter is the operation name to be executed and to be appended in Select object

        Returns
            None
        """
        operation_name: str = self.operation_name_in_path(path)
        if operation_name not in self.dict_all_operation().keys():
            msg: str = f"Error in path. This {operation_name} does not exists"
            raise PathError(msg, 400)
        return await self.dict_all_operation()[operation_name](*[path])

    def get_operation_names(self) -> list[str]:
        """Returns a list of function names. Each type of resource has different functions
            Returns
                list(str) - list function names
        """
        if self.function_names is None:
            self.function_names = self.resource.get_function_names()
        return self.function_names

    def entity_class(self) -> type[AlchemyBase]:
        """
        Returns the correspondent type of the entity class with the resource instance

        Returns
            type[AlchemyBase]
        """
        return self.resource.entity_class()

    def table(self) -> Table:
        """
        Returns the correspondent type of the entity class with the resource instance

        Returns
            type[AlchemyBase]
        """
        return self.entity_class().table()

    def attribute_names(self) -> list[str]:
        """
        Returns a list of attribute names
        Returns list(str)

        """
        return [name for name, attrib in self.entity_class().attributes_with_dereferenceable()]

    def column_name_given(self, attribute_name: str) -> str:
        """Returns the column name´s, given entity_class attribute name´s
        Parameters:
            attribute_name (str) - The attribute name´s
        Returns  (str)
        """
        return self.entity_class().column_name(attribute_name)

    def operation_name_in_path(self, path: str) -> str:
        operation_name_or_attribute_comma: str = first_word(path)
        if ',' in operation_name_or_attribute_comma or operation_name_or_attribute_comma in self.attribute_names():
            return 'projection'
        if operation_name_or_attribute_comma in self.get_operation_names():
            return operation_name_or_attribute_comma
        msg = f"This {path} is incorrect"
        print(msg)
        raise PathError(msg, 400)

    async def select_statement(self) -> Select:
        """Returns a Select object from paths
        Returns
        (Select)"""

        for path in self.paths:
            await self.execute_operation(path)
        self.select = self.get_select()
        return self.get_select()

    async def execute_statement(self) -> object:
        """Execute statement from path
        Returns
            Depends on result of sql statement"""
        await self.select_statement()
        print(self.get_select())
        if self.has_only_one_aggregate_math_function():
            res = await self.fetch_one()
            return res[0] if res is not None else 0
        else:
            rows = await self.fetch_all()
            return await self.rows_as_dict(rows)

    async def rows_as_dict(self, rows) -> list[dict]:
        return [await self.dialect_db().convert_row_to_dict(row) for row in rows]

    def alias_column(self, inst_attr: InstrumentedAttribute) -> object:
        if self.entity_class().is_relationship_fk_attribute(inst_attr) and self.prefix_column is not None:
            col = self.entity_class().column(inst_attr)
            model_class = self.entity_class().class_given_relationship_fk(inst_attr)
            prefix_model: str = f"{self.prefix_column}{model_class.router_list()}/"
            a_case = case((inst_attr is not None, col._rconcat(prefix_model)), else_=None).label(f"{self.entity_class().attribute_name_given(inst_attr)}")
            return a_case
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

    def columns_alias(self, attr_names: list[str] | None = None) -> list:
        if attr_names:
            attributes = [self.entity_class().__dict__[name] for name in attr_names if name in self.entity_class().__dict__.keys()]
        else:
            attributes = [ attr for name, attr in self.entity_class().attributes_with_dereferenceable()]
        list_col = []
        for att in attributes:
            col: Column | None = self.alias_column(att)
            if col is not None:
                list_col.append(col)
        return list_col

    def query(self) -> str:
        return str(self.get_select().compile(bind=self.db(), compile_kwargs={"literal_binds": True}))

    def subquery(self):
        return self.get_select().subquery().compile(bind=self.db(), compile_kwargs={"literal_binds": True})
