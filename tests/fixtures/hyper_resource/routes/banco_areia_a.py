from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.banco_areia_a import BancoAreiaAResource, BancoAreiaACollectionResource

def banco_areia_a_routes(app):
    
    @app.route(BancoAreiaAResource.router_id())
    async def banco_areia_a_id(request, id):
        r = BancoAreiaAResource(request)
        return await r.get_representation(id)
    
    @app.route(BancoAreiaAResource.router_id_path())
    async def banco_areia_a_resource_id_path(request, id, path):
        r = BancoAreiaAResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(BancoAreiaAResource.router_id(), methods=['HEAD'])
    async def head_banco_areia_a_id(request, id):
        r = BancoAreiaAResource(request)
        return await r.head(id)
    
    @app.route(BancoAreiaAResource.router_id_path(), methods=['HEAD'])
    async def head_banco_areia_a_resource_id_path(request, id, path):
        r = BancoAreiaAResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(BancoAreiaAResource.router_id(), methods=['OPTIONS'])
    async def options_banco_areia_a_id(request, id):
        r = BancoAreiaAResource(request)
        return await r.options(id)
    
    @app.route(BancoAreiaAResource.router_id_path(), methods=['OPTIONS'])
    async def options_banco_areia_a_resource_id_path(request, id, path):
        r = BancoAreiaAResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(BancoAreiaACollectionResource.router_list())
    async def banco_areia_a_list(request):
        cr = BancoAreiaACollectionResource(request)
        return await cr.get_representation()
        
    @app.route(BancoAreiaACollectionResource.router_list_path())
    async def banco_areia_a_list_path(request, path):
        cr = BancoAreiaACollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(BancoAreiaACollectionResource.router_list(), methods=['HEAD'] )
    async def head_banco_areia_a_list(request):
        cr = BancoAreiaACollectionResource(request)
        return await cr.head()

    @app.route(BancoAreiaACollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_banco_areia_a_list_path(request, path):
        cr = BancoAreiaACollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(BancoAreiaACollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_banco_areia_a_list(request):
        cr = BancoAreiaACollectionResource(request)
        return await cr.options()

    @app.route(BancoAreiaACollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_banco_areia_a_list_path(request, path):
        cr = BancoAreiaACollectionResource(request)
        return await cr.options_given_path(path)     
