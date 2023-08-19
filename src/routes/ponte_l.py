from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.ponte_l import PonteLResource, PonteLCollectionResource

def ponte_l_routes(app):
    
    @app.route(PonteLResource.router_id())
    async def ponte_l_id(request, id):
        r = PonteLResource(request)
        return await r.get_representation(id)
    
    @app.route(PonteLResource.router_id_path())
    async def ponte_l_resource_id_path(request, id, path):
        r = PonteLResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(PonteLResource.router_id(), methods=['HEAD'])
    async def head_ponte_l_id(request, id):
        r = PonteLResource(request)
        return await r.head(id)
    
    @app.route(PonteLResource.router_id_path(), methods=['HEAD'])
    async def head_ponte_l_resource_id_path(request, id, path):
        r = PonteLResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(PonteLResource.router_id(), methods=['OPTIONS'])
    async def options_ponte_l_id(request, id):
        r = PonteLResource(request)
        return await r.options(id)
    
    @app.route(PonteLResource.router_id_path(), methods=['OPTIONS'])
    async def options_ponte_l_resource_id_path(request, id, path):
        r = PonteLResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(PonteLCollectionResource.router_list())
    async def ponte_l_list(request):
        cr = PonteLCollectionResource(request)
        return await cr.get_representation()
        
    @app.route(PonteLCollectionResource.router_list_path())
    async def ponte_l_list_path(request, path):
        cr = PonteLCollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(PonteLCollectionResource.router_list(), methods=['HEAD'] )
    async def head_ponte_l_list(request):
        cr = PonteLCollectionResource(request)
        return await cr.head()

    @app.route(PonteLCollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_ponte_l_list_path(request, path):
        cr = PonteLCollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(PonteLCollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_ponte_l_list(request):
        cr = PonteLCollectionResource(request)
        return await cr.options()

    @app.route(PonteLCollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_ponte_l_list_path(request, path):
        cr = PonteLCollectionResource(request)
        return await cr.options_given_path(path)     
