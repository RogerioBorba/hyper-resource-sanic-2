from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.curva_batimetrica_l import CurvaBatimetricaLResource, CurvaBatimetricaLCollectionResource

def curva_batimetrica_l_routes(app):
    
    @app.route(CurvaBatimetricaLResource.router_id())
    async def curva_batimetrica_l_id(request, id):
        r = CurvaBatimetricaLResource(request)
        return await r.get_representation(id)
    
    @app.route(CurvaBatimetricaLResource.router_id_path())
    async def curva_batimetrica_l_resource_id_path(request, id, path):
        r = CurvaBatimetricaLResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(CurvaBatimetricaLResource.router_id(), methods=['HEAD'])
    async def head_curva_batimetrica_l_id(request, id):
        r = CurvaBatimetricaLResource(request)
        return await r.head(id)
    
    @app.route(CurvaBatimetricaLResource.router_id_path(), methods=['HEAD'])
    async def head_curva_batimetrica_l_resource_id_path(request, id, path):
        r = CurvaBatimetricaLResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(CurvaBatimetricaLResource.router_id(), methods=['OPTIONS'])
    async def options_curva_batimetrica_l_id(request, id):
        r = CurvaBatimetricaLResource(request)
        return await r.options(id)
    
    @app.route(CurvaBatimetricaLResource.router_id_path(), methods=['OPTIONS'])
    async def options_curva_batimetrica_l_resource_id_path(request, id, path):
        r = CurvaBatimetricaLResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(CurvaBatimetricaLCollectionResource.router_list())
    async def curva_batimetrica_l_list(request):
        cr = CurvaBatimetricaLCollectionResource(request)
        return await cr.get_representation()
        
    @app.route(CurvaBatimetricaLCollectionResource.router_list_path())
    async def curva_batimetrica_l_list_path(request, path):
        cr = CurvaBatimetricaLCollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(CurvaBatimetricaLCollectionResource.router_list(), methods=['HEAD'] )
    async def head_curva_batimetrica_l_list(request):
        cr = CurvaBatimetricaLCollectionResource(request)
        return await cr.head()

    @app.route(CurvaBatimetricaLCollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_curva_batimetrica_l_list_path(request, path):
        cr = CurvaBatimetricaLCollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(CurvaBatimetricaLCollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_curva_batimetrica_l_list(request):
        cr = CurvaBatimetricaLCollectionResource(request)
        return await cr.options()

    @app.route(CurvaBatimetricaLCollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_curva_batimetrica_l_list_path(request, path):
        cr = CurvaBatimetricaLCollectionResource(request)
        return await cr.options_given_path(path)     
