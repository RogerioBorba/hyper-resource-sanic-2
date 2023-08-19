from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.rocha_em_agua_a import RochaEmAguaAResource, RochaEmAguaACollectionResource

def rocha_em_agua_a_routes(app):
    
    @app.route(RochaEmAguaAResource.router_id())
    async def rocha_em_agua_a_id(request, id):
        r = RochaEmAguaAResource(request)
        return await r.get_representation(id)
    
    @app.route(RochaEmAguaAResource.router_id_path())
    async def rocha_em_agua_a_resource_id_path(request, id, path):
        r = RochaEmAguaAResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(RochaEmAguaAResource.router_id(), methods=['HEAD'])
    async def head_rocha_em_agua_a_id(request, id):
        r = RochaEmAguaAResource(request)
        return await r.head(id)
    
    @app.route(RochaEmAguaAResource.router_id_path(), methods=['HEAD'])
    async def head_rocha_em_agua_a_resource_id_path(request, id, path):
        r = RochaEmAguaAResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(RochaEmAguaAResource.router_id(), methods=['OPTIONS'])
    async def options_rocha_em_agua_a_id(request, id):
        r = RochaEmAguaAResource(request)
        return await r.options(id)
    
    @app.route(RochaEmAguaAResource.router_id_path(), methods=['OPTIONS'])
    async def options_rocha_em_agua_a_resource_id_path(request, id, path):
        r = RochaEmAguaAResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(RochaEmAguaACollectionResource.router_list())
    async def rocha_em_agua_a_list(request):
        cr = RochaEmAguaACollectionResource(request)
        return await cr.get_representation()
        
    @app.route(RochaEmAguaACollectionResource.router_list_path())
    async def rocha_em_agua_a_list_path(request, path):
        cr = RochaEmAguaACollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(RochaEmAguaACollectionResource.router_list(), methods=['HEAD'] )
    async def head_rocha_em_agua_a_list(request):
        cr = RochaEmAguaACollectionResource(request)
        return await cr.head()

    @app.route(RochaEmAguaACollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_rocha_em_agua_a_list_path(request, path):
        cr = RochaEmAguaACollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(RochaEmAguaACollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_rocha_em_agua_a_list(request):
        cr = RochaEmAguaACollectionResource(request)
        return await cr.options()

    @app.route(RochaEmAguaACollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_rocha_em_agua_a_list_path(request, path):
        cr = RochaEmAguaACollectionResource(request)
        return await cr.options_given_path(path)     
