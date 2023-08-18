from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.recife_a import RecifeAResource, RecifeACollectionResource

def recife_a_routes(app):
    
    @app.route(RecifeAResource.router_id())
    async def recife_a_id(request, id):
        r = RecifeAResource(request)
        return await r.get_representation(id)
    
    @app.route(RecifeAResource.router_id_path())
    async def recife_a_resource_id_path(request, id, path):
        r = RecifeAResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(RecifeAResource.router_id(), methods=['HEAD'])
    async def head_recife_a_id(request, id):
        r = RecifeAResource(request)
        return await r.head(id)
    
    @app.route(RecifeAResource.router_id_path(), methods=['HEAD'])
    async def head_recife_a_resource_id_path(request, id, path):
        r = RecifeAResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(RecifeAResource.router_id(), methods=['OPTIONS'])
    async def options_recife_a_id(request, id):
        r = RecifeAResource(request)
        return await r.options(id)
    
    @app.route(RecifeAResource.router_id_path(), methods=['OPTIONS'])
    async def options_recife_a_resource_id_path(request, id, path):
        r = RecifeAResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(RecifeACollectionResource.router_list())
    async def recife_a_list(request):
        cr = RecifeACollectionResource(request)
        return await cr.get_representation()
        
    @app.route(RecifeACollectionResource.router_list_path())
    async def recife_a_list_path(request, path):
        cr = RecifeACollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(RecifeACollectionResource.router_list(), methods=['HEAD'] )
    async def head_recife_a_list(request):
        cr = RecifeACollectionResource(request)
        return await cr.head()

    @app.route(RecifeACollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_recife_a_list_path(request, path):
        cr = RecifeACollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(RecifeACollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_recife_a_list(request):
        cr = RecifeACollectionResource(request)
        return await cr.options()

    @app.route(RecifeACollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_recife_a_list_path(request, path):
        cr = RecifeACollectionResource(request)
        return await cr.options_given_path(path)     
