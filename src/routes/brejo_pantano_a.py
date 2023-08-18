from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.brejo_pantano_a import BrejoPantanoAResource, BrejoPantanoACollectionResource

def brejo_pantano_a_routes(app):
    
    @app.route(BrejoPantanoAResource.router_id())
    async def brejo_pantano_a_id(request, id):
        r = BrejoPantanoAResource(request)
        return await r.get_representation(id)
    
    @app.route(BrejoPantanoAResource.router_id_path())
    async def brejo_pantano_a_resource_id_path(request, id, path):
        r = BrejoPantanoAResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(BrejoPantanoAResource.router_id(), methods=['HEAD'])
    async def head_brejo_pantano_a_id(request, id):
        r = BrejoPantanoAResource(request)
        return await r.head(id)
    
    @app.route(BrejoPantanoAResource.router_id_path(), methods=['HEAD'])
    async def head_brejo_pantano_a_resource_id_path(request, id, path):
        r = BrejoPantanoAResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(BrejoPantanoAResource.router_id(), methods=['OPTIONS'])
    async def options_brejo_pantano_a_id(request, id):
        r = BrejoPantanoAResource(request)
        return await r.options(id)
    
    @app.route(BrejoPantanoAResource.router_id_path(), methods=['OPTIONS'])
    async def options_brejo_pantano_a_resource_id_path(request, id, path):
        r = BrejoPantanoAResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(BrejoPantanoACollectionResource.router_list())
    async def brejo_pantano_a_list(request):
        cr = BrejoPantanoACollectionResource(request)
        return await cr.get_representation()
        
    @app.route(BrejoPantanoACollectionResource.router_list_path())
    async def brejo_pantano_a_list_path(request, path):
        cr = BrejoPantanoACollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(BrejoPantanoACollectionResource.router_list(), methods=['HEAD'] )
    async def head_brejo_pantano_a_list(request):
        cr = BrejoPantanoACollectionResource(request)
        return await cr.head()

    @app.route(BrejoPantanoACollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_brejo_pantano_a_list_path(request, path):
        cr = BrejoPantanoACollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(BrejoPantanoACollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_brejo_pantano_a_list(request):
        cr = BrejoPantanoACollectionResource(request)
        return await cr.options()

    @app.route(BrejoPantanoACollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_brejo_pantano_a_list_path(request, path):
        cr = BrejoPantanoACollectionResource(request)
        return await cr.options_given_path(path)     
