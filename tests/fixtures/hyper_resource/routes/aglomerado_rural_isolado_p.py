from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.aglomerado_rural_isolado_p import AglomeradoRuralIsoladoPResource, AglomeradoRuralIsoladoPCollectionResource

def aglomerado_rural_isolado_p_routes(app):
    
    @app.route(AglomeradoRuralIsoladoPResource.router_id())
    async def aglomerado_rural_isolado_p_id(request, id):
        r = AglomeradoRuralIsoladoPResource(request)
        return await r.get_representation(id)
    
    @app.route(AglomeradoRuralIsoladoPResource.router_id_path())
    async def aglomerado_rural_isolado_p_resource_id_path(request, id, path):
        r = AglomeradoRuralIsoladoPResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(AglomeradoRuralIsoladoPResource.router_id(), methods=['HEAD'])
    async def head_aglomerado_rural_isolado_p_id(request, id):
        r = AglomeradoRuralIsoladoPResource(request)
        return await r.head(id)
    
    @app.route(AglomeradoRuralIsoladoPResource.router_id_path(), methods=['HEAD'])
    async def head_aglomerado_rural_isolado_p_resource_id_path(request, id, path):
        r = AglomeradoRuralIsoladoPResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(AglomeradoRuralIsoladoPResource.router_id(), methods=['OPTIONS'])
    async def options_aglomerado_rural_isolado_p_id(request, id):
        r = AglomeradoRuralIsoladoPResource(request)
        return await r.options(id)
    
    @app.route(AglomeradoRuralIsoladoPResource.router_id_path(), methods=['OPTIONS'])
    async def options_aglomerado_rural_isolado_p_resource_id_path(request, id, path):
        r = AglomeradoRuralIsoladoPResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(AglomeradoRuralIsoladoPCollectionResource.router_list())
    async def aglomerado_rural_isolado_p_list(request):
        cr = AglomeradoRuralIsoladoPCollectionResource(request)
        return await cr.get_representation()
        
    @app.route(AglomeradoRuralIsoladoPCollectionResource.router_list_path())
    async def aglomerado_rural_isolado_p_list_path(request, path):
        cr = AglomeradoRuralIsoladoPCollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(AglomeradoRuralIsoladoPCollectionResource.router_list(), methods=['HEAD'] )
    async def head_aglomerado_rural_isolado_p_list(request):
        cr = AglomeradoRuralIsoladoPCollectionResource(request)
        return await cr.head()

    @app.route(AglomeradoRuralIsoladoPCollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_aglomerado_rural_isolado_p_list_path(request, path):
        cr = AglomeradoRuralIsoladoPCollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(AglomeradoRuralIsoladoPCollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_aglomerado_rural_isolado_p_list(request):
        cr = AglomeradoRuralIsoladoPCollectionResource(request)
        return await cr.options()

    @app.route(AglomeradoRuralIsoladoPCollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_aglomerado_rural_isolado_p_list_path(request, path):
        cr = AglomeradoRuralIsoladoPCollectionResource(request)
        return await cr.options_given_path(path)     
