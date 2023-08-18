from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.sinalizacao_p import SinalizacaoPResource, SinalizacaoPCollectionResource

def sinalizacao_p_routes(app):
    
    @app.route(SinalizacaoPResource.router_id())
    async def sinalizacao_p_id(request, id):
        r = SinalizacaoPResource(request)
        return await r.get_representation(id)
    
    @app.route(SinalizacaoPResource.router_id_path())
    async def sinalizacao_p_resource_id_path(request, id, path):
        r = SinalizacaoPResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(SinalizacaoPResource.router_id(), methods=['HEAD'])
    async def head_sinalizacao_p_id(request, id):
        r = SinalizacaoPResource(request)
        return await r.head(id)
    
    @app.route(SinalizacaoPResource.router_id_path(), methods=['HEAD'])
    async def head_sinalizacao_p_resource_id_path(request, id, path):
        r = SinalizacaoPResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(SinalizacaoPResource.router_id(), methods=['OPTIONS'])
    async def options_sinalizacao_p_id(request, id):
        r = SinalizacaoPResource(request)
        return await r.options(id)
    
    @app.route(SinalizacaoPResource.router_id_path(), methods=['OPTIONS'])
    async def options_sinalizacao_p_resource_id_path(request, id, path):
        r = SinalizacaoPResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(SinalizacaoPCollectionResource.router_list())
    async def sinalizacao_p_list(request):
        cr = SinalizacaoPCollectionResource(request)
        return await cr.get_representation()
        
    @app.route(SinalizacaoPCollectionResource.router_list_path())
    async def sinalizacao_p_list_path(request, path):
        cr = SinalizacaoPCollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(SinalizacaoPCollectionResource.router_list(), methods=['HEAD'] )
    async def head_sinalizacao_p_list(request):
        cr = SinalizacaoPCollectionResource(request)
        return await cr.head()

    @app.route(SinalizacaoPCollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_sinalizacao_p_list_path(request, path):
        cr = SinalizacaoPCollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(SinalizacaoPCollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_sinalizacao_p_list(request):
        cr = SinalizacaoPCollectionResource(request)
        return await cr.options()

    @app.route(SinalizacaoPCollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_sinalizacao_p_list_path(request, path):
        cr = SinalizacaoPCollectionResource(request)
        return await cr.options_given_path(path)     
