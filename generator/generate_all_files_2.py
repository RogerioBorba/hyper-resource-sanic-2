import os
import inspect
import importlib
import argparse
from generator.generate_model_sqlalchemy import Generator
from generator.generate_static import generate_all_static_files
from generator.generator_context import generate_all_context_files
from generator.generator_resource import generate_all_resource_files
from generator.generator_route import generate_all_router_files, generate_all_entry_point_file
from src.orm.models import AlchemyBase, Base
from src.orm.geo_models import AlchemyGeoBase

def load_model_classes():
    """
    Load dynamically all classes in the models folder and return a list of class

    Returns:
        list
    """
    # Lista todos os arquivos na pasta
    #path_models = f"{os.getcwd()}\\src\\models"
    path_models: str = f"C:\desenv\python-des\hyper-resource-sanic-2\src\models"
    files_on_models_folder = os.listdir(path_models)
    # Filtra os arquivos com a extensão .py
    modules_py = [a_file[:-3] for a_file in files_on_models_folder if a_file.endswith(".py") and not a_file.startswith("__init__")]
    # Importa cada módulo dinamicamente
    path_module: str = path_models[2:].replace('\\', '.')[1:]
    all_modules = []
    for name_module in modules_py:
        modulo = importlib.import_module(f"src.models.{name_module}")
        #all_modules.append(modulo)
        contents = inspect.getmembers(modulo, inspect.isclass)
        all_modules.extend([(name, _class) for name, _class in contents  if issubclass(_class, Base ) and _class != Base and _class != AlchemyBase and _class != AlchemyGeoBase])
    return all_modules


def main():
    parser = argparse.ArgumentParser(description="Programa para gerar classes")
    parser.add_argument("--schema", required=True, help="Esquema")
    parser.add_argument("--db_url", required=True, help="URL do banco de dados")
    parser.add_argument("--remove_prefix", required=False, help="Remove prefix of the class")
    parser.add_argument("--remove_suffix", required=False, help="Remove suffix of the class")
    parser.add_argument("--latin1", required=False, help="Includes latin-1 in the beginning of the file")
    parser.add_argument( "--post", action="store_true", required=False,
                         help="Generates routes for http method post" )
    parser.add_argument("--patch_put", action="store_true", required=False,   help="Generates routes for http methods patch and put")
    parser.add_argument("--delete", action="store_true", required=False, help="Generates routes for http methods  delete")

    args = parser.parse_args()
    g = Generator(args.db_url, args.schema)
    print(g.all_column_type())
    #exit(1)
    print(f"Generating model files ...")
    # generate_all_model_files(clsmodels)
    g.generate_model_files(remove_prefix=args.remove_prefix, remove_suffix=args.remove_suffix, latin1=args.latin1)
    clsmodels: list[[str, type]] = load_model_classes()
    generate_all_context_files(clsmodels)
    print("Generating context files ...")

    # Generate all resources
    print("Generating resource files ...")
    generate_all_resource_files(clsmodels)#, is_geo)

    # Generate all routes
    print("Generating route files ...")
    generate_all_router_files(clsmodels, args.patch_put, args.post, args.delete)

    # Generate entrypoint file
    print("Generating entrypoint file...")
    generate_all_entry_point_file(clsmodels)

    # Generate all static files
    print("Generating all static files...")
    generate_all_static_files(clsmodels)#), is_geo)


if __name__ == "__main__":
    # python -m generator.generate_all_files_2 --schema bcim --db_url postgresql://postgres:desenv@127.0.0.1:5432/postgis --remove_prefix True --latin1 True
    main()




