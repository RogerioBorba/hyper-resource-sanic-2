import os
from itertools import chain

from geoalchemy2 import Geometry
from sqlalchemy import Float, String, ForeignKey, Integer, Double, Boolean, Date, BIGINT, ARRAY
from sqlalchemy import INTEGER, SMALLINT, NUMERIC, FLOAT, DOUBLE, REAL, DOUBLE_PRECISION, VARCHAR, CHAR, TEXT, DATE, BOOLEAN
from sqlalchemy import create_engine, MetaData, Table, Column
from sqlalchemy.util import FacadeDict

from generator.util import convert_camel_case_to_underline


def str_latin_1() -> str:
    """Returns encoding string in latin-1 - first line

       Returns:
           str
    """
    return "# -*- coding: latin-1 -*-\n"


def is_geo_column(column: Column) -> bool:
    """returns True if column's type is Geometry, otherwise False

        Parameters:
            column (Column): a Column

        Returns:
            boolean
    """
    return type(column.type) == Geometry


def is_geo_table(table: Table) -> bool:
    """returns True if table has a geometry column, otherwise False

        Parameters:
            table (Table): a Table

        Returns:
            boolean
    """
    for column_name, column in table.columns.items():
        if is_geo_column(column):
            return True
    return False


def convert_underline_to_camel_case(underline_string: str, remove_prefix: bool = False, remove_suffix: bool = False) -> str:
    snippets = underline_string.split("_")
    if remove_prefix and len(snippets) > 1:
        snippets = snippets[1:]
    if remove_suffix and len(snippets) > 1:
        snippets = snippets[:-1]
    capitalized_snippets = [s.capitalize() for s in snippets]
    return "".join(capitalized_snippets)


def str_python_type(column: Column) -> str:
    """returns a string representing the type in python.

        Parameters:
            column (Column): a Column from database
        Returns:
            str
    """
    d = {ARRAY: 'ARRAY',
         INTEGER: 'int',
         SMALLINT: 'int',
         BIGINT: 'int',
         FLOAT: 'float',
         DOUBLE_PRECISION: 'float',
         DOUBLE: 'float',
         REAL: 'float',
         NUMERIC: 'float',
         TEXT: 'str',
         VARCHAR: 'str',
         CHAR: 'str',
         DATE: 'Date',
         BOOLEAN: 'bool',
         Geometry: 'Geometry'
         }
    return d[type(column.type)] if type(column.type) in d else 'None'


def db_to_db_type(db_type: type) -> type:
    d = {ARRAY: ARRAY,
         INTEGER: Integer,
         SMALLINT: Integer,
         BIGINT: Integer,
         NUMERIC: Float,
         FLOAT: Float,
         DOUBLE: Double,
         DOUBLE_PRECISION: Double,
         REAL: Float,
         VARCHAR: String,
         CHAR: String,
         TEXT: String,
         DATE: Date,
         BOOLEAN: Boolean,
         Geometry: Geometry
         }
    return d[db_type] if db_type in d else None


def str_db_type(column: Column) -> str:
    """returns a string representing the type of column.

        Parameters:
            column (Column): a Column from database
        Returns:
            str
    """
    d = {ARRAY: 'ARRAY',
         INTEGER: 'Integer',
         SMALLINT: 'Integer',
         BIGINT: 'Integer',
         NUMERIC: 'Float',
         FLOAT: 'Float',
         DOUBLE: 'Double',
         REAL: 'Float',
         DOUBLE_PRECISION: 'Double',
         VARCHAR: 'String',
         CHAR: 'String',
         TEXT: 'String',
         DATE: 'Date',
         BOOLEAN: 'Boolean',
         Geometry: 'Geometry'
         }
    return d[type(column.type)] if type(column.type) in d else 'None'


def str_for_foreign_key_column(column: Column) -> str:
    """returns a string created from foreign key column (orm.Column).

        Parameters:
            column (Column): a Column from database
        Returns:
            str
    """
    fk_name: str = ''
    fk: ForeignKey = list(column.foreign_keys)[0]
    if column.table.schema:
        fk_name += fk.column.table.schema + '.'
    fk_name += fk.column.table.name + '.' + fk.column.table.primary_key.columns[0].name #column.name
    return f"ForeignKey('{fk_name}')"


def is_column_foreign_key(column: Column) -> bool:
    """ Returns bool checking if the column (orm.Column) is a Foreign key

        Parameters:
            column (Column): a Column from database
        Returns:
            bool
    """
    return bool(column.foreign_keys)


def mapped_col_content(column: Column) -> str:
    """returns a string representing content of the mapped_column,
    such as: ForeignKey("person.person_id"), primary_key=True.

        Parameters:
            column (Column): a Column from database
        Returns:
            str
    """
    str_type_column: str = f"{str_db_type(column)}('{column.type.geometry_type}')" if is_geo_column(column) else str_db_type(column)
    content: str = f"'{column.name}', {str_type_column}"
    comma: str = ", "
    if is_column_foreign_key(column):
        content += comma + str_for_foreign_key_column(column)
    if column.primary_key:
        content += comma + "primary_key=True"
    if column.index is not None:
        content += comma + "index=True"
    if column.unique is not None:
        content += comma + "unique=True"
    content += comma + f"nullable={column.nullable.__str__()}"
    return content


def str_mapping_relationship(column: Column, remove_prefix: bool = False, remove_suffix: bool = False) -> str:
    """returns a string created from foreign key column (orm.Column).

        Parameters:
            column (Column): a Column from database
            remove_prefix (bool): to remove the table_name prefix if True: Ex.: eco_ext_mineral_a => ExtMineralA
            remove_suffix (bool): to remove the table_name suffix if True: Ex.: eco_ext_mineral_a => EcoExtMineral

        Returns:
            str
    """
    attrib_name: str = column.name[3:] if column.name.startswith('id_') else column.name + '_rel'
    fk: ForeignKey = list(column.foreign_keys)[0]
    class_name: str = convert_underline_to_camel_case(fk.column.table.name, remove_prefix, remove_suffix)
    return f"{attrib_name}: Mapped['{class_name}'] = relationship('{class_name}', foreign_keys=[{column.name}])"


def str_mapping_attribute_column(column) -> str:
    """ Returns string such as => id: Mapped[Uuid] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4())

        Parameters:
            column (Column): a Column from database

        Returns:
            str
    """
    #id: Mapped[Uuid] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4())
    return f"{column.name}: Mapped[{str_python_type(column)}] = mapped_column({mapped_col_content(column)})"


def str_model_class_from(table: Table, remove_prefix: bool = False, remove_suffix: bool = False):
    """Generate a model class string from table

            Parameters:
                table (Table): a Table ( from orm sqlalchemy)
                remove_prefix (bool): to remove the table_name prefix if True: Ex.: eco_ext_mineral_a => ExtMineralA
                remove_suffix (bool): to remove the table_name suffix if True: Ex.: eco_ext_mineral_a => EcoExtMineral

            Returns:
                str
        """
    class_str: str = ""
    base_name: str = "AlchemyGeoBase" if is_geo_table(table) else "AlchemyBase"
    class_name: str = convert_underline_to_camel_case(table.name, remove_prefix, remove_suffix)
    class_str += f"class {class_name}({base_name}): \n"
    class_str += f"    __tablename__ = '{table.name}'\n"
    if table.schema:
        class_str += f"    __table_args__ = {{'schema': '{table.schema}'}}\n"
    class_str += "\n"
    for (name, column) in table.columns.items():
        class_str += f"    {str_mapping_attribute_column( column )}\n"
        if is_column_foreign_key(column):
            class_str += f"    {str_mapping_relationship( column, remove_prefix, remove_suffix )}\n"
    return class_str


def all_column_types_from(table: Table) -> list[type]:
    """returns all column types from tables
                Parameters:
                    table: (Table): Table from database
                Returns:
                    list(type)
            """
    return [type(column.type) for name, column in table.columns.items()]


def dict_module_types_from(table: Table) -> dict:
    """returns a dictionary where key is module of column type and value is list of type column
        Parameters:
            table: (Table): Table from database
        Returns:
            dictionary
    """
    d_module_tyes: dict = {}
    for tp in all_column_types_from(table):
        if tp.__module__ not in d_module_tyes:
            d_module_tyes[tp.__module__] = [db_to_db_type(tp)]
        else:
            if db_to_db_type(tp) not in d_module_tyes[tp.__module__]:
                list_type: list[type] = d_module_tyes[tp.__module__]
                list_type.append(db_to_db_type(tp))
                d_module_tyes[tp.__module__] = list_type
    return d_module_tyes


def str_imports_model(table: Table) -> str:
    """Generate imports to models as strings

            Parameters:
                table: (Table): Table fro database

            Returns:
                str
        """
    imports: str = ""
    for module_name, types in dict_module_types_from(table).items():
        as_comma_list_str: str = ','.join([tp.__name__ for tp in types])
        imports += f"from {module_name} import {as_comma_list_str}\n"
    return imports


def has_foreign_key(table: Table) -> bool:
    """ Returns bool checking if the table has a Foreign key

        Parameters:
            table (Table): a Column from database
        Returns:
            bool
    """
    for col_name, column in table.columns.items():
        if bool(column.foreign_keys):
            return True
    return False


def str_imports_foreign_key() -> str:
    """returns string with import ForeignKey and relationship

            Parameters:

            Returns:
                str
        """
    return "from sqlalchemy import ForeignKey\nfrom sqlalchemy.orm import relationship\n"


def str_imports_mapped() -> str:
    """
    returns string with import mapping. Ex.: from sqlalchemy.orm import Mapped, mapped_column

    Returns:
        str
    """
    return "from sqlalchemy.orm import Mapped, mapped_column\n"


def str_imports_mapping(table: Table) -> str:
    """returns string with import mapping. Ex.: from sqlalchemy.orm import Mapped, mapped_column, relationship

        Parameters:
            table (Table): a Table ( from orm sqlalchemy)

        Returns:
            str
    """
    relationship: str = ""
    f_key: str = ""
    if has_foreign_key(table):
        f_key = str_imports_foreign_key()
    return f"{f_key}{str_imports_mapped()}"


def str_imports_base(table: Table) -> str:
    """returns string with import to base class. Ex.: from sqlalchemy.orm import Mapped, mapped_column, relationship

            Parameters:
                table (Table): a Table ( from orm sqlalchemy)

            Returns:
                str
        """
    if is_geo_table(table):
        return f"from src.orm.geo_models import AlchemyGeoBase\n"
    return f"from src.orm.models import AlchemyBase\n"


def table_name(table: Table, remove_prefix: bool = False, remove_suffix: bool = False) -> str:
    """returns table name from Table

                Parameters:
                    table (Table): a Table ( from orm sqlalchemy)
                    remove_prefix (bool): to remove the table_name prefix if True: Ex.: eco_ext_mineral_a => ExtMineralA
                    remove_suffix (bool): to remove the table_name suffix if True: Ex.: eco_ext_mineral_a => EcoExtMineral

                Returns:
                    str
            """
    snippets = table.name.split("_")
    if remove_prefix and len( snippets ) > 1:
        snippets = snippets[1:]
    if remove_suffix and len( snippets ) > 1:
        snippets = snippets[:-1]
    return "_".join(snippets)


class Generator(object):
    def __init__(self, url_database: str, schema_name: str | None = None) -> None:
        """Class responsible to generate all sqlalchemy-models's class for

           Parameters:
               url_database (str): a string connection to database. Ex.: 'postgresql://user1:password1@127.0.0.1:5432/postgis'
               schema_name (str): schema name in the database if exists.
           Returns:
               None
        """
        self.url_database = url_database
        self.schema_name = schema_name
        self.engine = create_engine(self.url_database)
        self.metadata: MetaData = MetaData(schema=self.schema_name) if schema_name else MetaData()
        self.metadata.reflect(bind=self.engine)
        self.tables: FacadeDict = self.metadata.tables
        self.column_items: list[tuple[str, Column]] = list(chain.from_iterable([table.columns.items() for table_name, table in self.tables.items()]))

    def generate_model_class_from(self, table: Table, remove_prefix: bool = False, remove_suffix: bool = False, latin1: bool= False):
        """Generate a model class string from table

            Parameters:
                table (Table): a Table ( from orm sqlalchemy)
                remove_prefix (bool): to remove the table_name prefix if True: Ex.: eco_ext_mineral_a => ExtMineralA
                remove_suffix (bool): to remove the table_name suffix if True: Ex.: eco_ext_mineral_a => EcoExtMineral

            Returns:
                str
        """
        return (str_latin_1() if latin1 else "") +\
            str_imports_mapping(table) + \
            str_imports_model(table) + \
            str_imports_base(table) + \
            "\n\n" + \
            str_model_class_from(table, remove_prefix, remove_suffix)

    def generate_model_file_from(self,  table: Table, a_path: str | None = None, a_file_name: str | None = None, remove_prefix: bool = False, remove_suffix: bool = False, latin1: bool = False):
        path: str = a_path if a_path is not None else os.path.join(os.getcwd(), 'src', 'models')
        file_name: str = a_file_name if a_file_name is not None else convert_camel_case_to_underline(table_name(table, remove_prefix, remove_suffix)) #table_name(table, remove_prefix, remove_suffix)
        file_with_path = f'{path}\\{file_name}.py' #convert_camel_case_to_underline
        try:

            os.makedirs(path, exist_ok=True)
        except FileExistsError:
            pass
        finally:
            with open(file_with_path,'w') as file:
                file_content: str = self.generate_model_class_from(table, remove_prefix, remove_suffix, latin1)
                file.write(file_content)

    def generate_model_files(self, a_path: str | None = None, a_file_name: str | None = None,
                                  remove_prefix: bool = False, remove_suffix: bool = False,
                                  latin1: bool = False) -> None:
        """Generates all model classes in one file

            Parameters:
                a_path (str | None): directory that contains the models file
                a_file_name (str): The name of the file containing all classes
                remove_prefix (bool): to remove the table_name prefix if True: Ex.: eco_ext_mineral_a => ExtMineralA
                remove_suffix (bool): to remove the table_name suffix if True: Ex.: eco_ext_mineral_a => EcoExtMineral
                latin1 (bool): if true, insert latin-1 code in the beginning of the file

            Returns:
                None
        """
        for name, table in self.tables.items():
            self.generate_model_file_from(table=table, a_path=a_path, a_file_name=a_file_name, remove_prefix=remove_prefix, remove_suffix=remove_suffix, latin1=latin1)

    def all_column(self) -> list:
        lista = []
        for tab_name, table in self.tables.items():
            for (name, column) in table.columns.items():
                lista.append( column )
        return lista

    def all_column_type(self) -> list[type]:
        """returns a list with all columns types, without repetition, of all table

                    Parameters:

                    Returns:
                        list(type)
                """
        return list(set([type(column.type) for column in self.all_column()]))

    def dict_all_module_type(self) -> dict:
        d_module_tyes: dict = {}
        for tp in self.all_column_type():
            if tp.__module__ not in d_module_tyes:
                d_module_tyes[tp.__module__] = [db_to_db_type(tp)]

            else:
                if db_to_db_type(tp) not in d_module_tyes[tp.__module__]:
                    list_type: list[type] = d_module_tyes[tp.__module__]
                    list_type.append(db_to_db_type(tp))
                    d_module_tyes[tp.__module__] = list_type
        return d_module_tyes

    def is_any_column_foreign_key(self) -> bool:
        """
        returns true if some table has a fk column type

        Returns:
            bool
        """
        for col in self.all_column():
            if is_column_foreign_key(col):
                return True
        return False

    def str_imports_all_model(self) -> str:
        """Generate imports to models as strings

                Parameters:
                    table: (Table): Table fro database

                Returns:
                    str
            """
        imports: str = ""
        for module_name, types in self.dict_all_module_type().items():
            as_comma_list_str: str = ','.join([tp.__name__ for tp in types])
            imports += f"from {module_name} import {as_comma_list_str}\n"
        return imports

    def str_imports_base(self):
        """Generate imports to models from base class as strings.

            Returns:
                str
        """
        imports: str = ""
        if len([table for name, table in self.tables.items() if not is_geo_table(table)]):
            imports += "from src.orm.models import AlchemyBase\n"
        if len([table for name, table in self.tables.items() if is_geo_table(table)]):
            imports += "from src.orm.geo_models import AlchemyGeoBase\n"
        return imports

    def generate_all_model_class(self, remove_prefix: bool = False, remove_suffix: bool = False, latin1: bool = False):
        """Generate a model class string from table

            Parameters:
                remove_prefix (bool): to remove the table_name prefix if True: Ex.: eco_ext_mineral_a => ExtMineralA
                remove_suffix (bool): to remove the table_name suffix if True: Ex.: eco_ext_mineral_a => EcoExtMineral
                latin1 (bool): if rue create latin1 string in the begin

            Returns:
                str
        """
        str_models: str = ""
        str_models += str_latin_1() if latin1 else ""
        if self.is_any_column_foreign_key():
            str_models += str_imports_foreign_key()
        str_models += str_imports_mapped()
        str_models += self.str_imports_all_model()
        str_models += self.str_imports_base()
        for name, table in self.tables.items():
            str_models += "\n\n" + str_model_class_from(table, remove_prefix, remove_suffix)

        return str_models

    def generate_all_model_one_file(self, a_path: str | None = None, a_file_name: str = 'all_models', remove_prefix: bool = False, remove_suffix: bool = False, latin1: bool= False) -> None:
        """Generates all model classes in one file

                    Parameters:
                        a_path (str | None): directory that contains the models file
                        a_file_name (str): The name of the file containing all classes
                        remove_prefix (bool): to remove the table_name prefix if True: Ex.: eco_ext_mineral_a => ExtMineralA
                        remove_suffix (bool): to remove the table_name suffix if True: Ex.: eco_ext_mineral_a => EcoExtMineral
                        latin1 (bool): if true, insert latin-1 code in the beginning of the file

                    Returns:
                        None
                """
        path: str = a_path if a_path is not None else os.path.join(os.getcwd(), 'generator')
        file_name: str = a_file_name
        file_with_path = f'{path}\\{file_name}.py'
        try:

            os.makedirs(path, exist_ok=True)
        except FileExistsError:
            pass
        finally:
            print(f"Generating {file_with_path} ...")
            with open(file_with_path,'w') as file:
                file_content: str = self.generate_all_model_class(remove_prefix, remove_suffix, latin1)
                file.write(file_content)
