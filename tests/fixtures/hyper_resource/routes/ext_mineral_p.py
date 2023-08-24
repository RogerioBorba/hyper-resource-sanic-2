from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.ext_mineral_p import ExtMineralPResource, ExtMineralPCollectionResource

def ext_mineral_p_routes(app):
    
    @app.route(ExtMineralPResource.router_id())
    async def ext_mineral_p_id(request, id):
        r = ExtMineralPResource(request)
        return await r.get_representation(id)
    
    @app.route(ExtMineralPResource.router_id_path())
    async def ext_mineral_p_resource_id_path(request, id, path):
        r = ExtMineralPResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(ExtMineralPResource.router_id(), methods=['HEAD'])
    async def head_ext_mineral_p_id(request, id):
        r = ExtMineralPResource(request)
        return await r.head(id)
    
    @app.route(ExtMineralPResource.router_id_path(), methods=['HEAD'])
    async def head_ext_mineral_p_resource_id_path(request, id, path):
        r = ExtMineralPResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(ExtMineralPResource.router_id(), methods=['OPTIONS'])
    async def options_ext_mineral_p_id(request, id):
        r = ExtMineralPResource(request)
        return await r.options(id)
    
    @app.route(ExtMineralPResource.router_id_path(), methods=['OPTIONS'])
    async def options_ext_mineral_p_resource_id_path(request, id, path):
        r = ExtMineralPResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(ExtMineralPCollectionResource.router_list())
    async def ext_mineral_p_list(request):
        cr = ExtMineralPCollectionResource(request)
        return await cr.get_representation()
        
    @app.route(ExtMineralPCollectionResource.router_list_path())
    async def ext_mineral_p_list_path(request, path):
        cr = ExtMineralPCollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(ExtMineralPCollectionResource.router_list(), methods=['HEAD'] )
    async def head_ext_mineral_p_list(request):
        cr = ExtMineralPCollectionResource(request)
        return await cr.head()

    @app.route(ExtMineralPCollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_ext_mineral_p_list_path(request, path):
        cr = ExtMineralPCollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(ExtMineralPCollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_ext_mineral_p_list(request):
        cr = ExtMineralPCollectionResource(request)
        return await cr.options()

    @app.route(ExtMineralPCollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_ext_mineral_p_list_path(request, path):
        cr = ExtMineralPCollectionResource(request)
        return await cr.options_given_path(path)     
