from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.ponto_cotado_altimetrico_p import PontoCotadoAltimetricoPResource, PontoCotadoAltimetricoPCollectionResource

def ponto_cotado_altimetrico_p_routes(app):
    
    @app.route(PontoCotadoAltimetricoPResource.router_id())
    async def ponto_cotado_altimetrico_p_id(request, id):
        r = PontoCotadoAltimetricoPResource(request)
        return await r.get_representation(id)
    
    @app.route(PontoCotadoAltimetricoPResource.router_id_path())
    async def ponto_cotado_altimetrico_p_resource_id_path(request, id, path):
        r = PontoCotadoAltimetricoPResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(PontoCotadoAltimetricoPResource.router_id(), methods=['HEAD'])
    async def head_ponto_cotado_altimetrico_p_id(request, id):
        r = PontoCotadoAltimetricoPResource(request)
        return await r.head(id)
    
    @app.route(PontoCotadoAltimetricoPResource.router_id_path(), methods=['HEAD'])
    async def head_ponto_cotado_altimetrico_p_resource_id_path(request, id, path):
        r = PontoCotadoAltimetricoPResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(PontoCotadoAltimetricoPResource.router_id(), methods=['OPTIONS'])
    async def options_ponto_cotado_altimetrico_p_id(request, id):
        r = PontoCotadoAltimetricoPResource(request)
        return await r.options(id)
    
    @app.route(PontoCotadoAltimetricoPResource.router_id_path(), methods=['OPTIONS'])
    async def options_ponto_cotado_altimetrico_p_resource_id_path(request, id, path):
        r = PontoCotadoAltimetricoPResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(PontoCotadoAltimetricoPCollectionResource.router_list())
    async def ponto_cotado_altimetrico_p_list(request):
        cr = PontoCotadoAltimetricoPCollectionResource(request)
        return await cr.get_representation()
        
    @app.route(PontoCotadoAltimetricoPCollectionResource.router_list_path())
    async def ponto_cotado_altimetrico_p_list_path(request, path):
        cr = PontoCotadoAltimetricoPCollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(PontoCotadoAltimetricoPCollectionResource.router_list(), methods=['HEAD'] )
    async def head_ponto_cotado_altimetrico_p_list(request):
        cr = PontoCotadoAltimetricoPCollectionResource(request)
        return await cr.head()

    @app.route(PontoCotadoAltimetricoPCollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_ponto_cotado_altimetrico_p_list_path(request, path):
        cr = PontoCotadoAltimetricoPCollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(PontoCotadoAltimetricoPCollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_ponto_cotado_altimetrico_p_list(request):
        cr = PontoCotadoAltimetricoPCollectionResource(request)
        return await cr.options()

    @app.route(PontoCotadoAltimetricoPCollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_ponto_cotado_altimetrico_p_list_path(request, path):
        cr = PontoCotadoAltimetricoPCollectionResource(request)
        return await cr.options_given_path(path)     
