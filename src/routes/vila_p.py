from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.vila_p import VilaPResource, VilaPCollectionResource

def vila_p_routes(app):
    
    @app.route(VilaPResource.router_id())
    async def vila_p_id(request, id):
        r = VilaPResource(request)
        return await r.get_representation(id)
    
    @app.route(VilaPResource.router_id_path())
    async def vila_p_resource_id_path(request, id, path):
        r = VilaPResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(VilaPResource.router_id(), methods=['HEAD'])
    async def head_vila_p_id(request, id):
        r = VilaPResource(request)
        return await r.head(id)
    
    @app.route(VilaPResource.router_id_path(), methods=['HEAD'])
    async def head_vila_p_resource_id_path(request, id, path):
        r = VilaPResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(VilaPResource.router_id(), methods=['OPTIONS'])
    async def options_vila_p_id(request, id):
        r = VilaPResource(request)
        return await r.options(id)
    
    @app.route(VilaPResource.router_id_path(), methods=['OPTIONS'])
    async def options_vila_p_resource_id_path(request, id, path):
        r = VilaPResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(VilaPCollectionResource.router_list())
    async def vila_p_list(request):
        cr = VilaPCollectionResource(request)
        return await cr.get_representation()
        
    @app.route(VilaPCollectionResource.router_list_path())
    async def vila_p_list_path(request, path):
        cr = VilaPCollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(VilaPCollectionResource.router_list(), methods=['HEAD'] )
    async def head_vila_p_list(request):
        cr = VilaPCollectionResource(request)
        return await cr.head()

    @app.route(VilaPCollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_vila_p_list_path(request, path):
        cr = VilaPCollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(VilaPCollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_vila_p_list(request):
        cr = VilaPCollectionResource(request)
        return await cr.options()

    @app.route(VilaPCollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_vila_p_list_path(request, path):
        cr = VilaPCollectionResource(request)
        return await cr.options_given_path(path)     
