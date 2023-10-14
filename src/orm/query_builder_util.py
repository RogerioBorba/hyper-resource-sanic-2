# -*- coding: latin-1 -*-
import re
from src.url_interpreter.interpreter_error import PathError
MAX: str = 'max'
MIN: str = 'min'
COUNT: str = 'count'
AVG: str = 'avg'
SUM: str = 'sum'
GROUPBY: str = 'groupby'
HAVING: str = 'having'
ORDERBY: str = 'orderby'
PROJECTION: str = 'projection'
LIMIT: str = 'limit'
OFFSET: str = 'offset'
OFFSETLIMIT: str = 'offsetlimit'
FILTER: str = 'filter'
COLLECT: str = 'collect'

HYPER_OPERATION_NAMES: list[str] = [MAX, MIN, COUNT, AVG, SUM, GROUPBY, HAVING, ORDERBY, PROJECTION, LIMIT,
                                    OFFSET, OFFSETLIMIT, FILTER, COLLECT]

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
    if len(path) == 0:
        return []
    path_local: str = path if path[0] != '/' else path[1:]
    partes: list[str] = re.split('''\/\*\/(?=(?:[^'"]|'[^']*'|"[^"]*")*$)''', path_local)
    return partes


def split_by_slash(path: str) -> list[str]:
    return re.split('''/(?=(?:[^'"]|'[^']*'|"[^"]*")*$)''', path)


def normalize_path_as_list_old(path: str, splitter: str = '/*/') -> list[str]:
    """Returns a list of path separated by splitter
    Parameters:
        path (str): a path from outside
        splitter (str): a separator string.
    Returns:
       A list(str) of path.
       Ex.: unidade-federacao-a-list/nome,sigla,geom/*/filter/sigla/in/ES,RJ/*/orderby/sigla
       ['unidade-federacao-a-list/nome,sigla,geom','filter/sigla/in/ES,RJ', 'orderby/sigla']

    """

    if len(path) == 0:
        return []
    path_local: str = path if path[0] != '/' else path[1:]
    paths: list[str] = path_local.split(splitter)
    return paths if paths[-1] != '' else paths[:-1]


def comma_list_str_as_list(str_list: str) -> list[str]:
    """Returns a list of string separated by comma
        Parameters:
            str_list (str): a path from outside
        Returns:
           A list(str) of string.
           Ex.: 'nome,sigla,geom' => ['nome', 'sigla', 'geom']
        """
    return str_list.lower().strip().split(',')


def normalize_sql_clause(path: str, clause_name: str) -> str:
    """
    remove the sql clause of the beginning and slash if exist at end of path.

    Parameters:
        path(str) - path have to be a clause sql. Ex.: orderby/name; projection/name,date
        clause_name (str) - is the clause in the path to remove

    Returns a (str)
    """
    local_path: str = path.lower()
    local_path = local_path[:-1] if local_path[-1] == '/' else local_path
    len_clause: int = len(f'{clause_name}/')
    return local_path[len_clause:] if local_path.startswith(f'{clause_name}/') else local_path


def path_without_last_slash(path: str) -> str:
    """
        Return a string without last slash if it exists.

        Parameters:
            path(str) - path have to be a clause sql.
            Ex.: orderby/name/ => orderby/name
            orderby/(/https://server/api/state/23/name/)/ => orderby/(/https://server/api/state/23/name/)/
        Returns a (str)
    """
    if path[-1] != '/':
        return path
    if path[:-1] == '/' and path[:-2] == ')':
        return path
    else:
        return path[:-1]


def path_as_list(path: str, ignore_last_slash: bool = True, splitter: str = '/') -> list[str]:
    """
        Return a list string without last slash if it exists.
        Parameters:
            path(str) - path should be a clause sql. Ex.: orderby/name/ => orderby/name
            ignore_last_slash(bool) - if is True does not consider last splitter to split the string
            splitter(str) = the character to split the string
        Returns a (str)
        """
    if ignore_last_slash:
        return path_without_last_slash(path).split(splitter)
    return path.split(splitter)
