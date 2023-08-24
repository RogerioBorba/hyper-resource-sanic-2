from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.travessia_p import TravessiaPResource, TravessiaPCollectionResource

def travessia_p_routes(app):
    
    @app.route(TravessiaPResource.router_id())
    async def travessia_p_id(request, id):
        r = TravessiaPResource(request)
        return await r.get_representation(id)
    
    @app.route(TravessiaPResource.router_id_path())
    async def travessia_p_resource_id_path(request, id, path):
        r = TravessiaPResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(TravessiaPResource.router_id(), methods=['HEAD'])
    async def head_travessia_p_id(request, id):
        r = TravessiaPResource(request)
        return await r.head(id)
    
    @app.route(TravessiaPResource.router_id_path(), methods=['HEAD'])
    async def head_travessia_p_resource_id_path(request, id, path):
        r = TravessiaPResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(TravessiaPResource.router_id(), methods=['OPTIONS'])
    async def options_travessia_p_id(request, id):
        r = TravessiaPResource(request)
        return await r.options(id)
    
    @app.route(TravessiaPResource.router_id_path(), methods=['OPTIONS'])
    async def options_travessia_p_resource_id_path(request, id, path):
        r = TravessiaPResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(TravessiaPCollectionResource.router_list())
    async def travessia_p_list(request):
        cr = TravessiaPCollectionResource(request)
        return await cr.get_representation()
        
    @app.route(TravessiaPCollectionResource.router_list_path())
    async def travessia_p_list_path(request, path):
        cr = TravessiaPCollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(TravessiaPCollectionResource.router_list(), methods=['HEAD'] )
    async def head_travessia_p_list(request):
        cr = TravessiaPCollectionResource(request)
        return await cr.head()

    @app.route(TravessiaPCollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_travessia_p_list_path(request, path):
        cr = TravessiaPCollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(TravessiaPCollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_travessia_p_list(request):
        cr = TravessiaPCollectionResource(request)
        return await cr.options()

    @app.route(TravessiaPCollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_travessia_p_list_path(request, path):
        cr = TravessiaPCollectionResource(request)
        return await cr.options_given_path(path)     
