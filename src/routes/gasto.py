from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.gasto import GastoResource, GastoCollectionResource

def gasto_routes(app):
    
    @app.route(GastoResource.router_id())
    async def gasto_id(request, id):
        r = GastoResource(request)
        return await r.get_representation(id)
    
    @app.route(GastoResource.router_id_path())
    async def gasto_resource_id_path(request, id, path):
        r = GastoResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(GastoResource.router_id(), methods=['HEAD'])
    async def head_gasto_id(request, id):
        r = GastoResource(request)
        return await r.head(id)
    
    @app.route(GastoResource.router_id_path(), methods=['HEAD'])
    async def head_gasto_resource_id_path(request, id, path):
        r = GastoResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(GastoResource.router_id(), methods=['OPTIONS'])
    async def options_gasto_id(request, id):
        r = GastoResource(request)
        return await r.options(id)
    
    @app.route(GastoResource.router_id_path(), methods=['OPTIONS'])
    async def options_gasto_resource_id_path(request, id, path):
        r = GastoResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(GastoCollectionResource.router_list())
    async def gasto_list(request):
        cr = GastoCollectionResource(request)
        return await cr.get_representation()
        
    @app.route(GastoCollectionResource.router_list_path())
    async def gasto_list_path(request, path):
        cr = GastoCollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(GastoCollectionResource.router_list(), methods=['HEAD'] )
    async def head_gasto_list(request):
        cr = GastoCollectionResource(request)
        return await cr.head()

    @app.route(GastoCollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_gasto_list_path(request, path):
        cr = GastoCollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(GastoCollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_gasto_list(request):
        cr = GastoCollectionResource(request)
        return await cr.options()

    @app.route(GastoCollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_gasto_list_path(request, path):
        cr = GastoCollectionResource(request)
        return await cr.options_given_path(path)     
