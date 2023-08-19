from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.area_edificada_a import AreaEdificadaAResource, AreaEdificadaACollectionResource

def area_edificada_a_routes(app):
    
    @app.route(AreaEdificadaAResource.router_id())
    async def area_edificada_a_id(request, id):
        r = AreaEdificadaAResource(request)
        return await r.get_representation(id)
    
    @app.route(AreaEdificadaAResource.router_id_path())
    async def area_edificada_a_resource_id_path(request, id, path):
        r = AreaEdificadaAResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(AreaEdificadaAResource.router_id(), methods=['HEAD'])
    async def head_area_edificada_a_id(request, id):
        r = AreaEdificadaAResource(request)
        return await r.head(id)
    
    @app.route(AreaEdificadaAResource.router_id_path(), methods=['HEAD'])
    async def head_area_edificada_a_resource_id_path(request, id, path):
        r = AreaEdificadaAResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(AreaEdificadaAResource.router_id(), methods=['OPTIONS'])
    async def options_area_edificada_a_id(request, id):
        r = AreaEdificadaAResource(request)
        return await r.options(id)
    
    @app.route(AreaEdificadaAResource.router_id_path(), methods=['OPTIONS'])
    async def options_area_edificada_a_resource_id_path(request, id, path):
        r = AreaEdificadaAResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(AreaEdificadaACollectionResource.router_list())
    async def area_edificada_a_list(request):
        cr = AreaEdificadaACollectionResource(request)
        return await cr.get_representation()
        
    @app.route(AreaEdificadaACollectionResource.router_list_path())
    async def area_edificada_a_list_path(request, path):
        cr = AreaEdificadaACollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(AreaEdificadaACollectionResource.router_list(), methods=['HEAD'] )
    async def head_area_edificada_a_list(request):
        cr = AreaEdificadaACollectionResource(request)
        return await cr.head()

    @app.route(AreaEdificadaACollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_area_edificada_a_list_path(request, path):
        cr = AreaEdificadaACollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(AreaEdificadaACollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_area_edificada_a_list(request):
        cr = AreaEdificadaACollectionResource(request)
        return await cr.options()

    @app.route(AreaEdificadaACollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_area_edificada_a_list_path(request, path):
        cr = AreaEdificadaACollectionResource(request)
        return await cr.options_given_path(path)     
