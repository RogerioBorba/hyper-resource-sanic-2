from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.barragem_p import BarragemPResource, BarragemPCollectionResource

def barragem_p_routes(app):
    
    @app.route(BarragemPResource.router_id())
    async def barragem_p_id(request, id):
        r = BarragemPResource(request)
        return await r.get_representation(id)
    
    @app.route(BarragemPResource.router_id_path())
    async def barragem_p_resource_id_path(request, id, path):
        r = BarragemPResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(BarragemPResource.router_id(), methods=['HEAD'])
    async def head_barragem_p_id(request, id):
        r = BarragemPResource(request)
        return await r.head(id)
    
    @app.route(BarragemPResource.router_id_path(), methods=['HEAD'])
    async def head_barragem_p_resource_id_path(request, id, path):
        r = BarragemPResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(BarragemPResource.router_id(), methods=['OPTIONS'])
    async def options_barragem_p_id(request, id):
        r = BarragemPResource(request)
        return await r.options(id)
    
    @app.route(BarragemPResource.router_id_path(), methods=['OPTIONS'])
    async def options_barragem_p_resource_id_path(request, id, path):
        r = BarragemPResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(BarragemPCollectionResource.router_list())
    async def barragem_p_list(request):
        cr = BarragemPCollectionResource(request)
        return await cr.get_representation()
        
    @app.route(BarragemPCollectionResource.router_list_path())
    async def barragem_p_list_path(request, path):
        cr = BarragemPCollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(BarragemPCollectionResource.router_list(), methods=['HEAD'] )
    async def head_barragem_p_list(request):
        cr = BarragemPCollectionResource(request)
        return await cr.head()

    @app.route(BarragemPCollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_barragem_p_list_path(request, path):
        cr = BarragemPCollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(BarragemPCollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_barragem_p_list(request):
        cr = BarragemPCollectionResource(request)
        return await cr.options()

    @app.route(BarragemPCollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_barragem_p_list_path(request, path):
        cr = BarragemPCollectionResource(request)
        return await cr.options_given_path(path)     
