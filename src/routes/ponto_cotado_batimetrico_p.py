from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.ponto_cotado_batimetrico_p import PontoCotadoBatimetricoPResource, PontoCotadoBatimetricoPCollectionResource

def ponto_cotado_batimetrico_p_routes(app):
    
    @app.route(PontoCotadoBatimetricoPResource.router_id())
    async def ponto_cotado_batimetrico_p_id(request, id):
        r = PontoCotadoBatimetricoPResource(request)
        return await r.get_representation(id)
    
    @app.route(PontoCotadoBatimetricoPResource.router_id_path())
    async def ponto_cotado_batimetrico_p_resource_id_path(request, id, path):
        r = PontoCotadoBatimetricoPResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(PontoCotadoBatimetricoPResource.router_id(), methods=['HEAD'])
    async def head_ponto_cotado_batimetrico_p_id(request, id):
        r = PontoCotadoBatimetricoPResource(request)
        return await r.head(id)
    
    @app.route(PontoCotadoBatimetricoPResource.router_id_path(), methods=['HEAD'])
    async def head_ponto_cotado_batimetrico_p_resource_id_path(request, id, path):
        r = PontoCotadoBatimetricoPResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(PontoCotadoBatimetricoPResource.router_id(), methods=['OPTIONS'])
    async def options_ponto_cotado_batimetrico_p_id(request, id):
        r = PontoCotadoBatimetricoPResource(request)
        return await r.options(id)
    
    @app.route(PontoCotadoBatimetricoPResource.router_id_path(), methods=['OPTIONS'])
    async def options_ponto_cotado_batimetrico_p_resource_id_path(request, id, path):
        r = PontoCotadoBatimetricoPResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(PontoCotadoBatimetricoPCollectionResource.router_list())
    async def ponto_cotado_batimetrico_p_list(request):
        cr = PontoCotadoBatimetricoPCollectionResource(request)
        return await cr.get_representation()
        
    @app.route(PontoCotadoBatimetricoPCollectionResource.router_list_path())
    async def ponto_cotado_batimetrico_p_list_path(request, path):
        cr = PontoCotadoBatimetricoPCollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(PontoCotadoBatimetricoPCollectionResource.router_list(), methods=['HEAD'] )
    async def head_ponto_cotado_batimetrico_p_list(request):
        cr = PontoCotadoBatimetricoPCollectionResource(request)
        return await cr.head()

    @app.route(PontoCotadoBatimetricoPCollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_ponto_cotado_batimetrico_p_list_path(request, path):
        cr = PontoCotadoBatimetricoPCollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(PontoCotadoBatimetricoPCollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_ponto_cotado_batimetrico_p_list(request):
        cr = PontoCotadoBatimetricoPCollectionResource(request)
        return await cr.options()

    @app.route(PontoCotadoBatimetricoPCollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_ponto_cotado_batimetrico_p_list_path(request, path):
        cr = PontoCotadoBatimetricoPCollectionResource(request)
        return await cr.options_given_path(path)     
