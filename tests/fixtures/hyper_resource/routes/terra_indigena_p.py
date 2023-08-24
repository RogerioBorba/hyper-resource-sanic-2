from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.terra_indigena_p import TerraIndigenaPResource, TerraIndigenaPCollectionResource

def terra_indigena_p_routes(app):
    
    @app.route(TerraIndigenaPResource.router_id())
    async def terra_indigena_p_id(request, id):
        r = TerraIndigenaPResource(request)
        return await r.get_representation(id)
    
    @app.route(TerraIndigenaPResource.router_id_path())
    async def terra_indigena_p_resource_id_path(request, id, path):
        r = TerraIndigenaPResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(TerraIndigenaPResource.router_id(), methods=['HEAD'])
    async def head_terra_indigena_p_id(request, id):
        r = TerraIndigenaPResource(request)
        return await r.head(id)
    
    @app.route(TerraIndigenaPResource.router_id_path(), methods=['HEAD'])
    async def head_terra_indigena_p_resource_id_path(request, id, path):
        r = TerraIndigenaPResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(TerraIndigenaPResource.router_id(), methods=['OPTIONS'])
    async def options_terra_indigena_p_id(request, id):
        r = TerraIndigenaPResource(request)
        return await r.options(id)
    
    @app.route(TerraIndigenaPResource.router_id_path(), methods=['OPTIONS'])
    async def options_terra_indigena_p_resource_id_path(request, id, path):
        r = TerraIndigenaPResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(TerraIndigenaPCollectionResource.router_list())
    async def terra_indigena_p_list(request):
        cr = TerraIndigenaPCollectionResource(request)
        return await cr.get_representation()
        
    @app.route(TerraIndigenaPCollectionResource.router_list_path())
    async def terra_indigena_p_list_path(request, path):
        cr = TerraIndigenaPCollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(TerraIndigenaPCollectionResource.router_list(), methods=['HEAD'] )
    async def head_terra_indigena_p_list(request):
        cr = TerraIndigenaPCollectionResource(request)
        return await cr.head()

    @app.route(TerraIndigenaPCollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_terra_indigena_p_list_path(request, path):
        cr = TerraIndigenaPCollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(TerraIndigenaPCollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_terra_indigena_p_list(request):
        cr = TerraIndigenaPCollectionResource(request)
        return await cr.options()

    @app.route(TerraIndigenaPCollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_terra_indigena_p_list_path(request, path):
        cr = TerraIndigenaPCollectionResource(request)
        return await cr.options_given_path(path)     
