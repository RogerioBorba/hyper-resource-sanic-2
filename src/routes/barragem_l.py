from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.barragem_l import BarragemLResource, BarragemLCollectionResource

def barragem_l_routes(app):
    
    @app.route(BarragemLResource.router_id())
    async def barragem_l_id(request, id):
        r = BarragemLResource(request)
        return await r.get_representation(id)
    
    @app.route(BarragemLResource.router_id_path())
    async def barragem_l_resource_id_path(request, id, path):
        r = BarragemLResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(BarragemLResource.router_id(), methods=['HEAD'])
    async def head_barragem_l_id(request, id):
        r = BarragemLResource(request)
        return await r.head(id)
    
    @app.route(BarragemLResource.router_id_path(), methods=['HEAD'])
    async def head_barragem_l_resource_id_path(request, id, path):
        r = BarragemLResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(BarragemLResource.router_id(), methods=['OPTIONS'])
    async def options_barragem_l_id(request, id):
        r = BarragemLResource(request)
        return await r.options(id)
    
    @app.route(BarragemLResource.router_id_path(), methods=['OPTIONS'])
    async def options_barragem_l_resource_id_path(request, id, path):
        r = BarragemLResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(BarragemLCollectionResource.router_list())
    async def barragem_l_list(request):
        cr = BarragemLCollectionResource(request)
        return await cr.get_representation()
        
    @app.route(BarragemLCollectionResource.router_list_path())
    async def barragem_l_list_path(request, path):
        cr = BarragemLCollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(BarragemLCollectionResource.router_list(), methods=['HEAD'] )
    async def head_barragem_l_list(request):
        cr = BarragemLCollectionResource(request)
        return await cr.head()

    @app.route(BarragemLCollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_barragem_l_list_path(request, path):
        cr = BarragemLCollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(BarragemLCollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_barragem_l_list(request):
        cr = BarragemLCollectionResource(request)
        return await cr.options()

    @app.route(BarragemLCollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_barragem_l_list_path(request, path):
        cr = BarragemLCollectionResource(request)
        return await cr.options_given_path(path)     
