from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.municipio_pib import MunicipioPibResource, MunicipioPibCollectionResource

def municipio_pib_routes(app):
    
    @app.route("/municipios-pib/<id:int>")
    async def municipio_pib_id(request, id: int):
        r = MunicipioPibResource(request)
        return await r.get_representation(id)
    
    @app.route("/municipios-pib/<id:int>/<path:path>")
    async def municipio_pib_resource_id_path(request, id: int, path: str):
        r = MunicipioPibResource(request)
        return await r.get_representation_path(id, path)

    @app.route("/municipios-pib/<id:int>", methods=['OPTIONS'])
    async def options_municipio_pib_id(request, id):
        r = MunicipioPibResource(request)
        return await r.options(id)
    
    @app.route("/municipios-pib/<id:int>/<path:path>", methods=['OPTIONS'])
    async def options_municipio_pib_resource_id_path(request, id: int, path: str):
        r = MunicipioPibResource(request)
        return await r.options_given_path(id, path)
            
    @app.route("/municipios-pib")
    async def municipio_pib_list(request):
        cr = MunicipioPibCollectionResource(request)
        return await cr.get_representation()
        
    @app.route("/municipios-pib/<path:path>")
    async def municipio_pib_list_path(request, path: str):
        cr = MunicipioPibCollectionResource(request)
        return await cr.get_representation_path(path)

    @app.route("/municipios-pib", methods=['OPTIONS'] )
    async def options_municipio_pib_list(request):
        cr = MunicipioPibCollectionResource(request)
        return await cr.options()

    @app.route("/municipios-pib/<path:path>", methods=['OPTIONS'] )
    async def options_municipio_pib_list_path(request, path: str):
        cr = MunicipioPibCollectionResource(request)
        return await cr.options_path(path)
