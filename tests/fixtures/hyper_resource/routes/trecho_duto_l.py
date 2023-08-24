from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.trecho_duto_l import TrechoDutoLResource, TrechoDutoLCollectionResource

def trecho_duto_l_routes(app):
    
    @app.route(TrechoDutoLResource.router_id())
    async def trecho_duto_l_id(request, id):
        r = TrechoDutoLResource(request)
        return await r.get_representation(id)
    
    @app.route(TrechoDutoLResource.router_id_path())
    async def trecho_duto_l_resource_id_path(request, id, path):
        r = TrechoDutoLResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(TrechoDutoLResource.router_id(), methods=['HEAD'])
    async def head_trecho_duto_l_id(request, id):
        r = TrechoDutoLResource(request)
        return await r.head(id)
    
    @app.route(TrechoDutoLResource.router_id_path(), methods=['HEAD'])
    async def head_trecho_duto_l_resource_id_path(request, id, path):
        r = TrechoDutoLResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(TrechoDutoLResource.router_id(), methods=['OPTIONS'])
    async def options_trecho_duto_l_id(request, id):
        r = TrechoDutoLResource(request)
        return await r.options(id)
    
    @app.route(TrechoDutoLResource.router_id_path(), methods=['OPTIONS'])
    async def options_trecho_duto_l_resource_id_path(request, id, path):
        r = TrechoDutoLResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(TrechoDutoLCollectionResource.router_list())
    async def trecho_duto_l_list(request):
        cr = TrechoDutoLCollectionResource(request)
        return await cr.get_representation()
        
    @app.route(TrechoDutoLCollectionResource.router_list_path())
    async def trecho_duto_l_list_path(request, path):
        cr = TrechoDutoLCollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(TrechoDutoLCollectionResource.router_list(), methods=['HEAD'] )
    async def head_trecho_duto_l_list(request):
        cr = TrechoDutoLCollectionResource(request)
        return await cr.head()

    @app.route(TrechoDutoLCollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_trecho_duto_l_list_path(request, path):
        cr = TrechoDutoLCollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(TrechoDutoLCollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_trecho_duto_l_list(request):
        cr = TrechoDutoLCollectionResource(request)
        return await cr.options()

    @app.route(TrechoDutoLCollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_trecho_duto_l_list_path(request, path):
        cr = TrechoDutoLCollectionResource(request)
        return await cr.options_given_path(path)     
