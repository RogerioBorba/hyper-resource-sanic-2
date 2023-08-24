from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.tunel_l import TunelLResource, TunelLCollectionResource

def tunel_l_routes(app):
    
    @app.route(TunelLResource.router_id())
    async def tunel_l_id(request, id):
        r = TunelLResource(request)
        return await r.get_representation(id)
    
    @app.route(TunelLResource.router_id_path())
    async def tunel_l_resource_id_path(request, id, path):
        r = TunelLResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(TunelLResource.router_id(), methods=['HEAD'])
    async def head_tunel_l_id(request, id):
        r = TunelLResource(request)
        return await r.head(id)
    
    @app.route(TunelLResource.router_id_path(), methods=['HEAD'])
    async def head_tunel_l_resource_id_path(request, id, path):
        r = TunelLResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(TunelLResource.router_id(), methods=['OPTIONS'])
    async def options_tunel_l_id(request, id):
        r = TunelLResource(request)
        return await r.options(id)
    
    @app.route(TunelLResource.router_id_path(), methods=['OPTIONS'])
    async def options_tunel_l_resource_id_path(request, id, path):
        r = TunelLResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(TunelLCollectionResource.router_list())
    async def tunel_l_list(request):
        cr = TunelLCollectionResource(request)
        return await cr.get_representation()
        
    @app.route(TunelLCollectionResource.router_list_path())
    async def tunel_l_list_path(request, path):
        cr = TunelLCollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(TunelLCollectionResource.router_list(), methods=['HEAD'] )
    async def head_tunel_l_list(request):
        cr = TunelLCollectionResource(request)
        return await cr.head()

    @app.route(TunelLCollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_tunel_l_list_path(request, path):
        cr = TunelLCollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(TunelLCollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_tunel_l_list(request):
        cr = TunelLCollectionResource(request)
        return await cr.options()

    @app.route(TunelLCollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_tunel_l_list_path(request, path):
        cr = TunelLCollectionResource(request)
        return await cr.options_given_path(path)     
