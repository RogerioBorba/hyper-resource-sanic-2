from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.tipo_gasto import TipoGastoResource, TipoGastoCollectionResource

def tipo_gasto_routes(app):
    
    @app.route(TipoGastoResource.router_id())
    async def tipo_gasto_id(request, id):
        r = TipoGastoResource(request)
        return await r.get_representation(id)
    
    @app.route(TipoGastoResource.router_id_path())
    async def tipo_gasto_resource_id_path(request, id, path):
        r = TipoGastoResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(TipoGastoResource.router_id(), methods=['HEAD'])
    async def head_tipo_gasto_id(request, id):
        r = TipoGastoResource(request)
        return await r.head(id)
    
    @app.route(TipoGastoResource.router_id_path(), methods=['HEAD'])
    async def head_tipo_gasto_resource_id_path(request, id, path):
        r = TipoGastoResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(TipoGastoResource.router_id(), methods=['OPTIONS'])
    async def options_tipo_gasto_id(request, id):
        r = TipoGastoResource(request)
        return await r.options(id)
    
    @app.route(TipoGastoResource.router_id_path(), methods=['OPTIONS'])
    async def options_tipo_gasto_resource_id_path(request, id, path):
        r = TipoGastoResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(TipoGastoCollectionResource.router_list())
    async def tipo_gasto_list(request):
        cr = TipoGastoCollectionResource(request)
        return await cr.get_representation()
        
    @app.route(TipoGastoCollectionResource.router_list_path())
    async def tipo_gasto_list_path(request, path):
        cr = TipoGastoCollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(TipoGastoCollectionResource.router_list(), methods=['HEAD'] )
    async def head_tipo_gasto_list(request):
        cr = TipoGastoCollectionResource(request)
        return await cr.head()

    @app.route(TipoGastoCollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_tipo_gasto_list_path(request, path):
        cr = TipoGastoCollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(TipoGastoCollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_tipo_gasto_list(request):
        cr = TipoGastoCollectionResource(request)
        return await cr.options()

    @app.route(TipoGastoCollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_tipo_gasto_list_path(request, path):
        cr = TipoGastoCollectionResource(request)
        return await cr.options_given_path(path)     
