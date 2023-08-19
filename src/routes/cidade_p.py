from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.cidade_p import CidadePResource, CidadePCollectionResource

def cidade_p_routes(app):
    
    @app.route(CidadePResource.router_id())
    async def cidade_p_id(request, id):
        r = CidadePResource(request)
        return await r.get_representation(id)
    
    @app.route(CidadePResource.router_id_path())
    async def cidade_p_resource_id_path(request, id, path):
        r = CidadePResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(CidadePResource.router_id(), methods=['HEAD'])
    async def head_cidade_p_id(request, id):
        r = CidadePResource(request)
        return await r.head(id)
    
    @app.route(CidadePResource.router_id_path(), methods=['HEAD'])
    async def head_cidade_p_resource_id_path(request, id, path):
        r = CidadePResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(CidadePResource.router_id(), methods=['OPTIONS'])
    async def options_cidade_p_id(request, id):
        r = CidadePResource(request)
        return await r.options(id)
    
    @app.route(CidadePResource.router_id_path(), methods=['OPTIONS'])
    async def options_cidade_p_resource_id_path(request, id, path):
        r = CidadePResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(CidadePCollectionResource.router_list())
    async def cidade_p_list(request):
        cr = CidadePCollectionResource(request)
        return await cr.get_representation()
        
    @app.route(CidadePCollectionResource.router_list_path())
    async def cidade_p_list_path(request, path):
        cr = CidadePCollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(CidadePCollectionResource.router_list(), methods=['HEAD'] )
    async def head_cidade_p_list(request):
        cr = CidadePCollectionResource(request)
        return await cr.head()

    @app.route(CidadePCollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_cidade_p_list_path(request, path):
        cr = CidadePCollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(CidadePCollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_cidade_p_list(request):
        cr = CidadePCollectionResource(request)
        return await cr.options()

    @app.route(CidadePCollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_cidade_p_list_path(request, path):
        cr = CidadePCollectionResource(request)
        return await cr.options_given_path(path)     
