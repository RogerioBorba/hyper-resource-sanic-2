from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.pista_ponto_pouso_p import PistaPontoPousoPResource, PistaPontoPousoPCollectionResource

def pista_ponto_pouso_p_routes(app):
    
    @app.route(PistaPontoPousoPResource.router_id())
    async def pista_ponto_pouso_p_id(request, id):
        r = PistaPontoPousoPResource(request)
        return await r.get_representation(id)
    
    @app.route(PistaPontoPousoPResource.router_id_path())
    async def pista_ponto_pouso_p_resource_id_path(request, id, path):
        r = PistaPontoPousoPResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(PistaPontoPousoPResource.router_id(), methods=['HEAD'])
    async def head_pista_ponto_pouso_p_id(request, id):
        r = PistaPontoPousoPResource(request)
        return await r.head(id)
    
    @app.route(PistaPontoPousoPResource.router_id_path(), methods=['HEAD'])
    async def head_pista_ponto_pouso_p_resource_id_path(request, id, path):
        r = PistaPontoPousoPResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(PistaPontoPousoPResource.router_id(), methods=['OPTIONS'])
    async def options_pista_ponto_pouso_p_id(request, id):
        r = PistaPontoPousoPResource(request)
        return await r.options(id)
    
    @app.route(PistaPontoPousoPResource.router_id_path(), methods=['OPTIONS'])
    async def options_pista_ponto_pouso_p_resource_id_path(request, id, path):
        r = PistaPontoPousoPResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(PistaPontoPousoPCollectionResource.router_list())
    async def pista_ponto_pouso_p_list(request):
        cr = PistaPontoPousoPCollectionResource(request)
        return await cr.get_representation()
        
    @app.route(PistaPontoPousoPCollectionResource.router_list_path())
    async def pista_ponto_pouso_p_list_path(request, path):
        cr = PistaPontoPousoPCollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(PistaPontoPousoPCollectionResource.router_list(), methods=['HEAD'] )
    async def head_pista_ponto_pouso_p_list(request):
        cr = PistaPontoPousoPCollectionResource(request)
        return await cr.head()

    @app.route(PistaPontoPousoPCollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_pista_ponto_pouso_p_list_path(request, path):
        cr = PistaPontoPousoPCollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(PistaPontoPousoPCollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_pista_ponto_pouso_p_list(request):
        cr = PistaPontoPousoPCollectionResource(request)
        return await cr.options()

    @app.route(PistaPontoPousoPCollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_pista_ponto_pouso_p_list_path(request, path):
        cr = PistaPontoPousoPCollectionResource(request)
        return await cr.options_given_path(path)     
