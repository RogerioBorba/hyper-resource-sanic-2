from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.hidreletrica_p import HidreletricaPResource, HidreletricaPCollectionResource

def hidreletrica_p_routes(app):
    
    @app.route(HidreletricaPResource.router_id())
    async def hidreletrica_p_id(request, id):
        r = HidreletricaPResource(request)
        return await r.get_representation(id)
    
    @app.route(HidreletricaPResource.router_id_path())
    async def hidreletrica_p_resource_id_path(request, id, path):
        r = HidreletricaPResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(HidreletricaPResource.router_id(), methods=['HEAD'])
    async def head_hidreletrica_p_id(request, id):
        r = HidreletricaPResource(request)
        return await r.head(id)
    
    @app.route(HidreletricaPResource.router_id_path(), methods=['HEAD'])
    async def head_hidreletrica_p_resource_id_path(request, id, path):
        r = HidreletricaPResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(HidreletricaPResource.router_id(), methods=['OPTIONS'])
    async def options_hidreletrica_p_id(request, id):
        r = HidreletricaPResource(request)
        return await r.options(id)
    
    @app.route(HidreletricaPResource.router_id_path(), methods=['OPTIONS'])
    async def options_hidreletrica_p_resource_id_path(request, id, path):
        r = HidreletricaPResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(HidreletricaPCollectionResource.router_list())
    async def hidreletrica_p_list(request):
        cr = HidreletricaPCollectionResource(request)
        return await cr.get_representation()
        
    @app.route(HidreletricaPCollectionResource.router_list_path())
    async def hidreletrica_p_list_path(request, path):
        cr = HidreletricaPCollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(HidreletricaPCollectionResource.router_list(), methods=['HEAD'] )
    async def head_hidreletrica_p_list(request):
        cr = HidreletricaPCollectionResource(request)
        return await cr.head()

    @app.route(HidreletricaPCollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_hidreletrica_p_list_path(request, path):
        cr = HidreletricaPCollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(HidreletricaPCollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_hidreletrica_p_list(request):
        cr = HidreletricaPCollectionResource(request)
        return await cr.options()

    @app.route(HidreletricaPCollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_hidreletrica_p_list_path(request, path):
        cr = HidreletricaPCollectionResource(request)
        return await cr.options_given_path(path)     
