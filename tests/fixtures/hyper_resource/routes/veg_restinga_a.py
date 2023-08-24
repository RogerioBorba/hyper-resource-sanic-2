from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.veg_restinga_a import VegRestingaAResource, VegRestingaACollectionResource

def veg_restinga_a_routes(app):
    
    @app.route(VegRestingaAResource.router_id())
    async def veg_restinga_a_id(request, id):
        r = VegRestingaAResource(request)
        return await r.get_representation(id)
    
    @app.route(VegRestingaAResource.router_id_path())
    async def veg_restinga_a_resource_id_path(request, id, path):
        r = VegRestingaAResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(VegRestingaAResource.router_id(), methods=['HEAD'])
    async def head_veg_restinga_a_id(request, id):
        r = VegRestingaAResource(request)
        return await r.head(id)
    
    @app.route(VegRestingaAResource.router_id_path(), methods=['HEAD'])
    async def head_veg_restinga_a_resource_id_path(request, id, path):
        r = VegRestingaAResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(VegRestingaAResource.router_id(), methods=['OPTIONS'])
    async def options_veg_restinga_a_id(request, id):
        r = VegRestingaAResource(request)
        return await r.options(id)
    
    @app.route(VegRestingaAResource.router_id_path(), methods=['OPTIONS'])
    async def options_veg_restinga_a_resource_id_path(request, id, path):
        r = VegRestingaAResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(VegRestingaACollectionResource.router_list())
    async def veg_restinga_a_list(request):
        cr = VegRestingaACollectionResource(request)
        return await cr.get_representation()
        
    @app.route(VegRestingaACollectionResource.router_list_path())
    async def veg_restinga_a_list_path(request, path):
        cr = VegRestingaACollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(VegRestingaACollectionResource.router_list(), methods=['HEAD'] )
    async def head_veg_restinga_a_list(request):
        cr = VegRestingaACollectionResource(request)
        return await cr.head()

    @app.route(VegRestingaACollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_veg_restinga_a_list_path(request, path):
        cr = VegRestingaACollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(VegRestingaACollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_veg_restinga_a_list(request):
        cr = VegRestingaACollectionResource(request)
        return await cr.options()

    @app.route(VegRestingaACollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_veg_restinga_a_list_path(request, path):
        cr = VegRestingaACollectionResource(request)
        return await cr.options_given_path(path)     
