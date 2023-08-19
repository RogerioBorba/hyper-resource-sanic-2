from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.corredeira_l import CorredeiraLResource, CorredeiraLCollectionResource

def corredeira_l_routes(app):
    
    @app.route(CorredeiraLResource.router_id())
    async def corredeira_l_id(request, id):
        r = CorredeiraLResource(request)
        return await r.get_representation(id)
    
    @app.route(CorredeiraLResource.router_id_path())
    async def corredeira_l_resource_id_path(request, id, path):
        r = CorredeiraLResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(CorredeiraLResource.router_id(), methods=['HEAD'])
    async def head_corredeira_l_id(request, id):
        r = CorredeiraLResource(request)
        return await r.head(id)
    
    @app.route(CorredeiraLResource.router_id_path(), methods=['HEAD'])
    async def head_corredeira_l_resource_id_path(request, id, path):
        r = CorredeiraLResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(CorredeiraLResource.router_id(), methods=['OPTIONS'])
    async def options_corredeira_l_id(request, id):
        r = CorredeiraLResource(request)
        return await r.options(id)
    
    @app.route(CorredeiraLResource.router_id_path(), methods=['OPTIONS'])
    async def options_corredeira_l_resource_id_path(request, id, path):
        r = CorredeiraLResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(CorredeiraLCollectionResource.router_list())
    async def corredeira_l_list(request):
        cr = CorredeiraLCollectionResource(request)
        return await cr.get_representation()
        
    @app.route(CorredeiraLCollectionResource.router_list_path())
    async def corredeira_l_list_path(request, path):
        cr = CorredeiraLCollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(CorredeiraLCollectionResource.router_list(), methods=['HEAD'] )
    async def head_corredeira_l_list(request):
        cr = CorredeiraLCollectionResource(request)
        return await cr.head()

    @app.route(CorredeiraLCollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_corredeira_l_list_path(request, path):
        cr = CorredeiraLCollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(CorredeiraLCollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_corredeira_l_list(request):
        cr = CorredeiraLCollectionResource(request)
        return await cr.options()

    @app.route(CorredeiraLCollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_corredeira_l_list_path(request, path):
        cr = CorredeiraLCollectionResource(request)
        return await cr.options_given_path(path)     
