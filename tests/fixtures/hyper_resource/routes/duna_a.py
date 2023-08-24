from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.duna_a import DunaAResource, DunaACollectionResource

def duna_a_routes(app):
    
    @app.route(DunaAResource.router_id())
    async def duna_a_id(request, id):
        r = DunaAResource(request)
        return await r.get_representation(id)
    
    @app.route(DunaAResource.router_id_path())
    async def duna_a_resource_id_path(request, id, path):
        r = DunaAResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(DunaAResource.router_id(), methods=['HEAD'])
    async def head_duna_a_id(request, id):
        r = DunaAResource(request)
        return await r.head(id)
    
    @app.route(DunaAResource.router_id_path(), methods=['HEAD'])
    async def head_duna_a_resource_id_path(request, id, path):
        r = DunaAResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(DunaAResource.router_id(), methods=['OPTIONS'])
    async def options_duna_a_id(request, id):
        r = DunaAResource(request)
        return await r.options(id)
    
    @app.route(DunaAResource.router_id_path(), methods=['OPTIONS'])
    async def options_duna_a_resource_id_path(request, id, path):
        r = DunaAResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(DunaACollectionResource.router_list())
    async def duna_a_list(request):
        cr = DunaACollectionResource(request)
        return await cr.get_representation()
        
    @app.route(DunaACollectionResource.router_list_path())
    async def duna_a_list_path(request, path):
        cr = DunaACollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(DunaACollectionResource.router_list(), methods=['HEAD'] )
    async def head_duna_a_list(request):
        cr = DunaACollectionResource(request)
        return await cr.head()

    @app.route(DunaACollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_duna_a_list_path(request, path):
        cr = DunaACollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(DunaACollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_duna_a_list(request):
        cr = DunaACollectionResource(request)
        return await cr.options()

    @app.route(DunaACollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_duna_a_list_path(request, path):
        cr = DunaACollectionResource(request)
        return await cr.options_given_path(path)     
