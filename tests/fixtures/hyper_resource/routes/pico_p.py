from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.pico_p import PicoPResource, PicoPCollectionResource

def pico_p_routes(app):
    
    @app.route(PicoPResource.router_id())
    async def pico_p_id(request, id):
        r = PicoPResource(request)
        return await r.get_representation(id)
    
    @app.route(PicoPResource.router_id_path())
    async def pico_p_resource_id_path(request, id, path):
        r = PicoPResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(PicoPResource.router_id(), methods=['HEAD'])
    async def head_pico_p_id(request, id):
        r = PicoPResource(request)
        return await r.head(id)
    
    @app.route(PicoPResource.router_id_path(), methods=['HEAD'])
    async def head_pico_p_resource_id_path(request, id, path):
        r = PicoPResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(PicoPResource.router_id(), methods=['OPTIONS'])
    async def options_pico_p_id(request, id):
        r = PicoPResource(request)
        return await r.options(id)
    
    @app.route(PicoPResource.router_id_path(), methods=['OPTIONS'])
    async def options_pico_p_resource_id_path(request, id, path):
        r = PicoPResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(PicoPCollectionResource.router_list())
    async def pico_p_list(request):
        cr = PicoPCollectionResource(request)
        return await cr.get_representation()
        
    @app.route(PicoPCollectionResource.router_list_path())
    async def pico_p_list_path(request, path):
        cr = PicoPCollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(PicoPCollectionResource.router_list(), methods=['HEAD'] )
    async def head_pico_p_list(request):
        cr = PicoPCollectionResource(request)
        return await cr.head()

    @app.route(PicoPCollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_pico_p_list_path(request, path):
        cr = PicoPCollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(PicoPCollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_pico_p_list(request):
        cr = PicoPCollectionResource(request)
        return await cr.options()

    @app.route(PicoPCollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_pico_p_list_path(request, path):
        cr = PicoPCollectionResource(request)
        return await cr.options_given_path(path)     
