from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.sumidouro_vertedouro_p import SumidouroVertedouroPResource, SumidouroVertedouroPCollectionResource

def sumidouro_vertedouro_p_routes(app):
    
    @app.route(SumidouroVertedouroPResource.router_id())
    async def sumidouro_vertedouro_p_id(request, id):
        r = SumidouroVertedouroPResource(request)
        return await r.get_representation(id)
    
    @app.route(SumidouroVertedouroPResource.router_id_path())
    async def sumidouro_vertedouro_p_resource_id_path(request, id, path):
        r = SumidouroVertedouroPResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(SumidouroVertedouroPResource.router_id(), methods=['HEAD'])
    async def head_sumidouro_vertedouro_p_id(request, id):
        r = SumidouroVertedouroPResource(request)
        return await r.head(id)
    
    @app.route(SumidouroVertedouroPResource.router_id_path(), methods=['HEAD'])
    async def head_sumidouro_vertedouro_p_resource_id_path(request, id, path):
        r = SumidouroVertedouroPResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(SumidouroVertedouroPResource.router_id(), methods=['OPTIONS'])
    async def options_sumidouro_vertedouro_p_id(request, id):
        r = SumidouroVertedouroPResource(request)
        return await r.options(id)
    
    @app.route(SumidouroVertedouroPResource.router_id_path(), methods=['OPTIONS'])
    async def options_sumidouro_vertedouro_p_resource_id_path(request, id, path):
        r = SumidouroVertedouroPResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(SumidouroVertedouroPCollectionResource.router_list())
    async def sumidouro_vertedouro_p_list(request):
        cr = SumidouroVertedouroPCollectionResource(request)
        return await cr.get_representation()
        
    @app.route(SumidouroVertedouroPCollectionResource.router_list_path())
    async def sumidouro_vertedouro_p_list_path(request, path):
        cr = SumidouroVertedouroPCollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(SumidouroVertedouroPCollectionResource.router_list(), methods=['HEAD'] )
    async def head_sumidouro_vertedouro_p_list(request):
        cr = SumidouroVertedouroPCollectionResource(request)
        return await cr.head()

    @app.route(SumidouroVertedouroPCollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_sumidouro_vertedouro_p_list_path(request, path):
        cr = SumidouroVertedouroPCollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(SumidouroVertedouroPCollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_sumidouro_vertedouro_p_list(request):
        cr = SumidouroVertedouroPCollectionResource(request)
        return await cr.options()

    @app.route(SumidouroVertedouroPCollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_sumidouro_vertedouro_p_list_path(request, path):
        cr = SumidouroVertedouroPCollectionResource(request)
        return await cr.options_given_path(path)     
