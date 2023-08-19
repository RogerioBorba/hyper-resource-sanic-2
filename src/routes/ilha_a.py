from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.ilha_a import IlhaAResource, IlhaACollectionResource

def ilha_a_routes(app):
    
    @app.route(IlhaAResource.router_id())
    async def ilha_a_id(request, id):
        r = IlhaAResource(request)
        return await r.get_representation(id)
    
    @app.route(IlhaAResource.router_id_path())
    async def ilha_a_resource_id_path(request, id, path):
        r = IlhaAResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(IlhaAResource.router_id(), methods=['HEAD'])
    async def head_ilha_a_id(request, id):
        r = IlhaAResource(request)
        return await r.head(id)
    
    @app.route(IlhaAResource.router_id_path(), methods=['HEAD'])
    async def head_ilha_a_resource_id_path(request, id, path):
        r = IlhaAResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(IlhaAResource.router_id(), methods=['OPTIONS'])
    async def options_ilha_a_id(request, id):
        r = IlhaAResource(request)
        return await r.options(id)
    
    @app.route(IlhaAResource.router_id_path(), methods=['OPTIONS'])
    async def options_ilha_a_resource_id_path(request, id, path):
        r = IlhaAResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(IlhaACollectionResource.router_list())
    async def ilha_a_list(request):
        cr = IlhaACollectionResource(request)
        return await cr.get_representation()
        
    @app.route(IlhaACollectionResource.router_list_path())
    async def ilha_a_list_path(request, path):
        cr = IlhaACollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(IlhaACollectionResource.router_list(), methods=['HEAD'] )
    async def head_ilha_a_list(request):
        cr = IlhaACollectionResource(request)
        return await cr.head()

    @app.route(IlhaACollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_ilha_a_list_path(request, path):
        cr = IlhaACollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(IlhaACollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_ilha_a_list(request):
        cr = IlhaACollectionResource(request)
        return await cr.options()

    @app.route(IlhaACollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_ilha_a_list_path(request, path):
        cr = IlhaACollectionResource(request)
        return await cr.options_given_path(path)     
