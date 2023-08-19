from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.eclusa_l import EclusaLResource, EclusaLCollectionResource

def eclusa_l_routes(app):
    
    @app.route(EclusaLResource.router_id())
    async def eclusa_l_id(request, id):
        r = EclusaLResource(request)
        return await r.get_representation(id)
    
    @app.route(EclusaLResource.router_id_path())
    async def eclusa_l_resource_id_path(request, id, path):
        r = EclusaLResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(EclusaLResource.router_id(), methods=['HEAD'])
    async def head_eclusa_l_id(request, id):
        r = EclusaLResource(request)
        return await r.head(id)
    
    @app.route(EclusaLResource.router_id_path(), methods=['HEAD'])
    async def head_eclusa_l_resource_id_path(request, id, path):
        r = EclusaLResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(EclusaLResource.router_id(), methods=['OPTIONS'])
    async def options_eclusa_l_id(request, id):
        r = EclusaLResource(request)
        return await r.options(id)
    
    @app.route(EclusaLResource.router_id_path(), methods=['OPTIONS'])
    async def options_eclusa_l_resource_id_path(request, id, path):
        r = EclusaLResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(EclusaLCollectionResource.router_list())
    async def eclusa_l_list(request):
        cr = EclusaLCollectionResource(request)
        return await cr.get_representation()
        
    @app.route(EclusaLCollectionResource.router_list_path())
    async def eclusa_l_list_path(request, path):
        cr = EclusaLCollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(EclusaLCollectionResource.router_list(), methods=['HEAD'] )
    async def head_eclusa_l_list(request):
        cr = EclusaLCollectionResource(request)
        return await cr.head()

    @app.route(EclusaLCollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_eclusa_l_list_path(request, path):
        cr = EclusaLCollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(EclusaLCollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_eclusa_l_list(request):
        cr = EclusaLCollectionResource(request)
        return await cr.options()

    @app.route(EclusaLCollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_eclusa_l_list_path(request, path):
        cr = EclusaLCollectionResource(request)
        return await cr.options_given_path(path)     
