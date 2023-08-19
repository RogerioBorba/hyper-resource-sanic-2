from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.outros_limites_oficiais_l import OutrosLimitesOficiaisLResource, OutrosLimitesOficiaisLCollectionResource

def outros_limites_oficiais_l_routes(app):
    
    @app.route(OutrosLimitesOficiaisLResource.router_id())
    async def outros_limites_oficiais_l_id(request, id):
        r = OutrosLimitesOficiaisLResource(request)
        return await r.get_representation(id)
    
    @app.route(OutrosLimitesOficiaisLResource.router_id_path())
    async def outros_limites_oficiais_l_resource_id_path(request, id, path):
        r = OutrosLimitesOficiaisLResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(OutrosLimitesOficiaisLResource.router_id(), methods=['HEAD'])
    async def head_outros_limites_oficiais_l_id(request, id):
        r = OutrosLimitesOficiaisLResource(request)
        return await r.head(id)
    
    @app.route(OutrosLimitesOficiaisLResource.router_id_path(), methods=['HEAD'])
    async def head_outros_limites_oficiais_l_resource_id_path(request, id, path):
        r = OutrosLimitesOficiaisLResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(OutrosLimitesOficiaisLResource.router_id(), methods=['OPTIONS'])
    async def options_outros_limites_oficiais_l_id(request, id):
        r = OutrosLimitesOficiaisLResource(request)
        return await r.options(id)
    
    @app.route(OutrosLimitesOficiaisLResource.router_id_path(), methods=['OPTIONS'])
    async def options_outros_limites_oficiais_l_resource_id_path(request, id, path):
        r = OutrosLimitesOficiaisLResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(OutrosLimitesOficiaisLCollectionResource.router_list())
    async def outros_limites_oficiais_l_list(request):
        cr = OutrosLimitesOficiaisLCollectionResource(request)
        return await cr.get_representation()
        
    @app.route(OutrosLimitesOficiaisLCollectionResource.router_list_path())
    async def outros_limites_oficiais_l_list_path(request, path):
        cr = OutrosLimitesOficiaisLCollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(OutrosLimitesOficiaisLCollectionResource.router_list(), methods=['HEAD'] )
    async def head_outros_limites_oficiais_l_list(request):
        cr = OutrosLimitesOficiaisLCollectionResource(request)
        return await cr.head()

    @app.route(OutrosLimitesOficiaisLCollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_outros_limites_oficiais_l_list_path(request, path):
        cr = OutrosLimitesOficiaisLCollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(OutrosLimitesOficiaisLCollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_outros_limites_oficiais_l_list(request):
        cr = OutrosLimitesOficiaisLCollectionResource(request)
        return await cr.options()

    @app.route(OutrosLimitesOficiaisLCollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_outros_limites_oficiais_l_list_path(request, path):
        cr = OutrosLimitesOficiaisLCollectionResource(request)
        return await cr.options_given_path(path)     
