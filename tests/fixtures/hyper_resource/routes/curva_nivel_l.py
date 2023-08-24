from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.curva_nivel_l import CurvaNivelLResource, CurvaNivelLCollectionResource

def curva_nivel_l_routes(app):
    
    @app.route(CurvaNivelLResource.router_id())
    async def curva_nivel_l_id(request, id):
        r = CurvaNivelLResource(request)
        return await r.get_representation(id)
    
    @app.route(CurvaNivelLResource.router_id_path())
    async def curva_nivel_l_resource_id_path(request, id, path):
        r = CurvaNivelLResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(CurvaNivelLResource.router_id(), methods=['HEAD'])
    async def head_curva_nivel_l_id(request, id):
        r = CurvaNivelLResource(request)
        return await r.head(id)
    
    @app.route(CurvaNivelLResource.router_id_path(), methods=['HEAD'])
    async def head_curva_nivel_l_resource_id_path(request, id, path):
        r = CurvaNivelLResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(CurvaNivelLResource.router_id(), methods=['OPTIONS'])
    async def options_curva_nivel_l_id(request, id):
        r = CurvaNivelLResource(request)
        return await r.options(id)
    
    @app.route(CurvaNivelLResource.router_id_path(), methods=['OPTIONS'])
    async def options_curva_nivel_l_resource_id_path(request, id, path):
        r = CurvaNivelLResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(CurvaNivelLCollectionResource.router_list())
    async def curva_nivel_l_list(request):
        cr = CurvaNivelLCollectionResource(request)
        return await cr.get_representation()
        
    @app.route(CurvaNivelLCollectionResource.router_list_path())
    async def curva_nivel_l_list_path(request, path):
        cr = CurvaNivelLCollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(CurvaNivelLCollectionResource.router_list(), methods=['HEAD'] )
    async def head_curva_nivel_l_list(request):
        cr = CurvaNivelLCollectionResource(request)
        return await cr.head()

    @app.route(CurvaNivelLCollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_curva_nivel_l_list_path(request, path):
        cr = CurvaNivelLCollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(CurvaNivelLCollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_curva_nivel_l_list(request):
        cr = CurvaNivelLCollectionResource(request)
        return await cr.options()

    @app.route(CurvaNivelLCollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_curva_nivel_l_list_path(request, path):
        cr = CurvaNivelLCollectionResource(request)
        return await cr.options_given_path(path)     
