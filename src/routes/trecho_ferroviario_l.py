from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.trecho_ferroviario_l import TrechoFerroviarioLResource, TrechoFerroviarioLCollectionResource

def trecho_ferroviario_l_routes(app):
    
    @app.route(TrechoFerroviarioLResource.router_id())
    async def trecho_ferroviario_l_id(request, id):
        r = TrechoFerroviarioLResource(request)
        return await r.get_representation(id)
    
    @app.route(TrechoFerroviarioLResource.router_id_path())
    async def trecho_ferroviario_l_resource_id_path(request, id, path):
        r = TrechoFerroviarioLResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(TrechoFerroviarioLResource.router_id(), methods=['HEAD'])
    async def head_trecho_ferroviario_l_id(request, id):
        r = TrechoFerroviarioLResource(request)
        return await r.head(id)
    
    @app.route(TrechoFerroviarioLResource.router_id_path(), methods=['HEAD'])
    async def head_trecho_ferroviario_l_resource_id_path(request, id, path):
        r = TrechoFerroviarioLResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(TrechoFerroviarioLResource.router_id(), methods=['OPTIONS'])
    async def options_trecho_ferroviario_l_id(request, id):
        r = TrechoFerroviarioLResource(request)
        return await r.options(id)
    
    @app.route(TrechoFerroviarioLResource.router_id_path(), methods=['OPTIONS'])
    async def options_trecho_ferroviario_l_resource_id_path(request, id, path):
        r = TrechoFerroviarioLResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(TrechoFerroviarioLCollectionResource.router_list())
    async def trecho_ferroviario_l_list(request):
        cr = TrechoFerroviarioLCollectionResource(request)
        return await cr.get_representation()
        
    @app.route(TrechoFerroviarioLCollectionResource.router_list_path())
    async def trecho_ferroviario_l_list_path(request, path):
        cr = TrechoFerroviarioLCollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(TrechoFerroviarioLCollectionResource.router_list(), methods=['HEAD'] )
    async def head_trecho_ferroviario_l_list(request):
        cr = TrechoFerroviarioLCollectionResource(request)
        return await cr.head()

    @app.route(TrechoFerroviarioLCollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_trecho_ferroviario_l_list_path(request, path):
        cr = TrechoFerroviarioLCollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(TrechoFerroviarioLCollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_trecho_ferroviario_l_list(request):
        cr = TrechoFerroviarioLCollectionResource(request)
        return await cr.options()

    @app.route(TrechoFerroviarioLCollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_trecho_ferroviario_l_list_path(request, path):
        cr = TrechoFerroviarioLCollectionResource(request)
        return await cr.options_given_path(path)     
