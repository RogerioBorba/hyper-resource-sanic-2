from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.pais_a import PaisAResource, PaisACollectionResource

def pais_a_routes(app):
    
    @app.route(PaisAResource.router_id())
    async def pais_a_id(request, id):
        r = PaisAResource(request)
        return await r.get_representation(id)
    
    @app.route(PaisAResource.router_id_path())
    async def pais_a_resource_id_path(request, id, path):
        r = PaisAResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(PaisAResource.router_id(), methods=['HEAD'])
    async def head_pais_a_id(request, id):
        r = PaisAResource(request)
        return await r.head(id)
    
    @app.route(PaisAResource.router_id_path(), methods=['HEAD'])
    async def head_pais_a_resource_id_path(request, id, path):
        r = PaisAResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(PaisAResource.router_id(), methods=['OPTIONS'])
    async def options_pais_a_id(request, id):
        r = PaisAResource(request)
        return await r.options(id)
    
    @app.route(PaisAResource.router_id_path(), methods=['OPTIONS'])
    async def options_pais_a_resource_id_path(request, id, path):
        r = PaisAResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(PaisACollectionResource.router_list())
    async def pais_a_list(request):
        cr = PaisACollectionResource(request)
        return await cr.get_representation()
        
    @app.route(PaisACollectionResource.router_list_path())
    async def pais_a_list_path(request, path):
        cr = PaisACollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(PaisACollectionResource.router_list(), methods=['HEAD'] )
    async def head_pais_a_list(request):
        cr = PaisACollectionResource(request)
        return await cr.head()

    @app.route(PaisACollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_pais_a_list_path(request, path):
        cr = PaisACollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(PaisACollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_pais_a_list(request):
        cr = PaisACollectionResource(request)
        return await cr.options()

    @app.route(PaisACollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_pais_a_list_path(request, path):
        cr = PaisACollectionResource(request)
        return await cr.options_given_path(path)     
