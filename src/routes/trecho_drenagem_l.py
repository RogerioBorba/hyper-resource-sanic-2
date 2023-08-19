from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.trecho_drenagem_l import TrechoDrenagemLResource, TrechoDrenagemLCollectionResource

def trecho_drenagem_l_routes(app):
    
    @app.route(TrechoDrenagemLResource.router_id())
    async def trecho_drenagem_l_id(request, id):
        r = TrechoDrenagemLResource(request)
        return await r.get_representation(id)
    
    @app.route(TrechoDrenagemLResource.router_id_path())
    async def trecho_drenagem_l_resource_id_path(request, id, path):
        r = TrechoDrenagemLResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(TrechoDrenagemLResource.router_id(), methods=['HEAD'])
    async def head_trecho_drenagem_l_id(request, id):
        r = TrechoDrenagemLResource(request)
        return await r.head(id)
    
    @app.route(TrechoDrenagemLResource.router_id_path(), methods=['HEAD'])
    async def head_trecho_drenagem_l_resource_id_path(request, id, path):
        r = TrechoDrenagemLResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(TrechoDrenagemLResource.router_id(), methods=['OPTIONS'])
    async def options_trecho_drenagem_l_id(request, id):
        r = TrechoDrenagemLResource(request)
        return await r.options(id)
    
    @app.route(TrechoDrenagemLResource.router_id_path(), methods=['OPTIONS'])
    async def options_trecho_drenagem_l_resource_id_path(request, id, path):
        r = TrechoDrenagemLResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(TrechoDrenagemLCollectionResource.router_list())
    async def trecho_drenagem_l_list(request):
        cr = TrechoDrenagemLCollectionResource(request)
        return await cr.get_representation()
        
    @app.route(TrechoDrenagemLCollectionResource.router_list_path())
    async def trecho_drenagem_l_list_path(request, path):
        cr = TrechoDrenagemLCollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(TrechoDrenagemLCollectionResource.router_list(), methods=['HEAD'] )
    async def head_trecho_drenagem_l_list(request):
        cr = TrechoDrenagemLCollectionResource(request)
        return await cr.head()

    @app.route(TrechoDrenagemLCollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_trecho_drenagem_l_list_path(request, path):
        cr = TrechoDrenagemLCollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(TrechoDrenagemLCollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_trecho_drenagem_l_list(request):
        cr = TrechoDrenagemLCollectionResource(request)
        return await cr.options()

    @app.route(TrechoDrenagemLCollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_trecho_drenagem_l_list_path(request, path):
        cr = TrechoDrenagemLCollectionResource(request)
        return await cr.options_given_path(path)     
