from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.ext_mineral_a import ExtMineralAResource, ExtMineralACollectionResource

def ext_mineral_a_routes(app):
    
    @app.route(ExtMineralAResource.router_id())
    async def ext_mineral_a_id(request, id):
        r = ExtMineralAResource(request)
        return await r.get_representation(id)
    
    @app.route(ExtMineralAResource.router_id_path())
    async def ext_mineral_a_resource_id_path(request, id, path):
        r = ExtMineralAResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(ExtMineralAResource.router_id(), methods=['HEAD'])
    async def head_ext_mineral_a_id(request, id):
        r = ExtMineralAResource(request)
        return await r.head(id)
    
    @app.route(ExtMineralAResource.router_id_path(), methods=['HEAD'])
    async def head_ext_mineral_a_resource_id_path(request, id, path):
        r = ExtMineralAResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(ExtMineralAResource.router_id(), methods=['OPTIONS'])
    async def options_ext_mineral_a_id(request, id):
        r = ExtMineralAResource(request)
        return await r.options(id)
    
    @app.route(ExtMineralAResource.router_id_path(), methods=['OPTIONS'])
    async def options_ext_mineral_a_resource_id_path(request, id, path):
        r = ExtMineralAResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(ExtMineralACollectionResource.router_list())
    async def ext_mineral_a_list(request):
        cr = ExtMineralACollectionResource(request)
        return await cr.get_representation()
        
    @app.route(ExtMineralACollectionResource.router_list_path())
    async def ext_mineral_a_list_path(request, path):
        cr = ExtMineralACollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(ExtMineralACollectionResource.router_list(), methods=['HEAD'] )
    async def head_ext_mineral_a_list(request):
        cr = ExtMineralACollectionResource(request)
        return await cr.head()

    @app.route(ExtMineralACollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_ext_mineral_a_list_path(request, path):
        cr = ExtMineralACollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(ExtMineralACollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_ext_mineral_a_list(request):
        cr = ExtMineralACollectionResource(request)
        return await cr.options()

    @app.route(ExtMineralACollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_ext_mineral_a_list_path(request, path):
        cr = ExtMineralACollectionResource(request)
        return await cr.options_given_path(path)     
