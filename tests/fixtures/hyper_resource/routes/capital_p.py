from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.capital_p import CapitalPResource, CapitalPCollectionResource

def capital_p_routes(app):
    
    @app.route(CapitalPResource.router_id())
    async def capital_p_id(request, id):
        r = CapitalPResource(request)
        return await r.get_representation(id)
    
    @app.route(CapitalPResource.router_id_path())
    async def capital_p_resource_id_path(request, id, path):
        r = CapitalPResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(CapitalPResource.router_id(), methods=['HEAD'])
    async def head_capital_p_id(request, id):
        r = CapitalPResource(request)
        return await r.head(id)
    
    @app.route(CapitalPResource.router_id_path(), methods=['HEAD'])
    async def head_capital_p_resource_id_path(request, id, path):
        r = CapitalPResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(CapitalPResource.router_id(), methods=['OPTIONS'])
    async def options_capital_p_id(request, id):
        r = CapitalPResource(request)
        return await r.options(id)
    
    @app.route(CapitalPResource.router_id_path(), methods=['OPTIONS'])
    async def options_capital_p_resource_id_path(request, id, path):
        r = CapitalPResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(CapitalPCollectionResource.router_list())
    async def capital_p_list(request):
        cr = CapitalPCollectionResource(request)
        return await cr.get_representation()
        
    @app.route(CapitalPCollectionResource.router_list_path())
    async def capital_p_list_path(request, path):
        cr = CapitalPCollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(CapitalPCollectionResource.router_list(), methods=['HEAD'] )
    async def head_capital_p_list(request):
        cr = CapitalPCollectionResource(request)
        return await cr.head()

    @app.route(CapitalPCollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_capital_p_list_path(request, path):
        cr = CapitalPCollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(CapitalPCollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_capital_p_list(request):
        cr = CapitalPCollectionResource(request)
        return await cr.options()

    @app.route(CapitalPCollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_capital_p_list_path(request, path):
        cr = CapitalPCollectionResource(request)
        return await cr.options_given_path(path)     
