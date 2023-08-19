from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.corredeira_p import CorredeiraPResource, CorredeiraPCollectionResource

def corredeira_p_routes(app):
    
    @app.route(CorredeiraPResource.router_id())
    async def corredeira_p_id(request, id):
        r = CorredeiraPResource(request)
        return await r.get_representation(id)
    
    @app.route(CorredeiraPResource.router_id_path())
    async def corredeira_p_resource_id_path(request, id, path):
        r = CorredeiraPResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(CorredeiraPResource.router_id(), methods=['HEAD'])
    async def head_corredeira_p_id(request, id):
        r = CorredeiraPResource(request)
        return await r.head(id)
    
    @app.route(CorredeiraPResource.router_id_path(), methods=['HEAD'])
    async def head_corredeira_p_resource_id_path(request, id, path):
        r = CorredeiraPResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(CorredeiraPResource.router_id(), methods=['OPTIONS'])
    async def options_corredeira_p_id(request, id):
        r = CorredeiraPResource(request)
        return await r.options(id)
    
    @app.route(CorredeiraPResource.router_id_path(), methods=['OPTIONS'])
    async def options_corredeira_p_resource_id_path(request, id, path):
        r = CorredeiraPResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(CorredeiraPCollectionResource.router_list())
    async def corredeira_p_list(request):
        cr = CorredeiraPCollectionResource(request)
        return await cr.get_representation()
        
    @app.route(CorredeiraPCollectionResource.router_list_path())
    async def corredeira_p_list_path(request, path):
        cr = CorredeiraPCollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(CorredeiraPCollectionResource.router_list(), methods=['HEAD'] )
    async def head_corredeira_p_list(request):
        cr = CorredeiraPCollectionResource(request)
        return await cr.head()

    @app.route(CorredeiraPCollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_corredeira_p_list_path(request, path):
        cr = CorredeiraPCollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(CorredeiraPCollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_corredeira_p_list(request):
        cr = CorredeiraPCollectionResource(request)
        return await cr.options()

    @app.route(CorredeiraPCollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_corredeira_p_list_path(request, path):
        cr = CorredeiraPCollectionResource(request)
        return await cr.options_given_path(path)     
