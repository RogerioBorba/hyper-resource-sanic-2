from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.terra_indigena_a import TerraIndigenaAResource, TerraIndigenaACollectionResource

def terra_indigena_a_routes(app):
    
    @app.route(TerraIndigenaAResource.router_id())
    async def terra_indigena_a_id(request, id):
        r = TerraIndigenaAResource(request)
        return await r.get_representation(id)
    
    @app.route(TerraIndigenaAResource.router_id_path())
    async def terra_indigena_a_resource_id_path(request, id, path):
        r = TerraIndigenaAResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(TerraIndigenaAResource.router_id(), methods=['HEAD'])
    async def head_terra_indigena_a_id(request, id):
        r = TerraIndigenaAResource(request)
        return await r.head(id)
    
    @app.route(TerraIndigenaAResource.router_id_path(), methods=['HEAD'])
    async def head_terra_indigena_a_resource_id_path(request, id, path):
        r = TerraIndigenaAResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(TerraIndigenaAResource.router_id(), methods=['OPTIONS'])
    async def options_terra_indigena_a_id(request, id):
        r = TerraIndigenaAResource(request)
        return await r.options(id)
    
    @app.route(TerraIndigenaAResource.router_id_path(), methods=['OPTIONS'])
    async def options_terra_indigena_a_resource_id_path(request, id, path):
        r = TerraIndigenaAResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(TerraIndigenaACollectionResource.router_list())
    async def terra_indigena_a_list(request):
        cr = TerraIndigenaACollectionResource(request)
        return await cr.get_representation()
        
    @app.route(TerraIndigenaACollectionResource.router_list_path())
    async def terra_indigena_a_list_path(request, path):
        cr = TerraIndigenaACollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(TerraIndigenaACollectionResource.router_list(), methods=['HEAD'] )
    async def head_terra_indigena_a_list(request):
        cr = TerraIndigenaACollectionResource(request)
        return await cr.head()

    @app.route(TerraIndigenaACollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_terra_indigena_a_list_path(request, path):
        cr = TerraIndigenaACollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(TerraIndigenaACollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_terra_indigena_a_list(request):
        cr = TerraIndigenaACollectionResource(request)
        return await cr.options()

    @app.route(TerraIndigenaACollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_terra_indigena_a_list_path(request, path):
        cr = TerraIndigenaACollectionResource(request)
        return await cr.options_given_path(path)     
