from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.travessia_l import TravessiaLResource, TravessiaLCollectionResource

def travessia_l_routes(app):
    
    @app.route(TravessiaLResource.router_id())
    async def travessia_l_id(request, id):
        r = TravessiaLResource(request)
        return await r.get_representation(id)
    
    @app.route(TravessiaLResource.router_id_path())
    async def travessia_l_resource_id_path(request, id, path):
        r = TravessiaLResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(TravessiaLResource.router_id(), methods=['HEAD'])
    async def head_travessia_l_id(request, id):
        r = TravessiaLResource(request)
        return await r.head(id)
    
    @app.route(TravessiaLResource.router_id_path(), methods=['HEAD'])
    async def head_travessia_l_resource_id_path(request, id, path):
        r = TravessiaLResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(TravessiaLResource.router_id(), methods=['OPTIONS'])
    async def options_travessia_l_id(request, id):
        r = TravessiaLResource(request)
        return await r.options(id)
    
    @app.route(TravessiaLResource.router_id_path(), methods=['OPTIONS'])
    async def options_travessia_l_resource_id_path(request, id, path):
        r = TravessiaLResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(TravessiaLCollectionResource.router_list())
    async def travessia_l_list(request):
        cr = TravessiaLCollectionResource(request)
        return await cr.get_representation()
        
    @app.route(TravessiaLCollectionResource.router_list_path())
    async def travessia_l_list_path(request, path):
        cr = TravessiaLCollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(TravessiaLCollectionResource.router_list(), methods=['HEAD'] )
    async def head_travessia_l_list(request):
        cr = TravessiaLCollectionResource(request)
        return await cr.head()

    @app.route(TravessiaLCollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_travessia_l_list_path(request, path):
        cr = TravessiaLCollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(TravessiaLCollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_travessia_l_list(request):
        cr = TravessiaLCollectionResource(request)
        return await cr.options()

    @app.route(TravessiaLCollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_travessia_l_list_path(request, path):
        cr = TravessiaLCollectionResource(request)
        return await cr.options_given_path(path)     
