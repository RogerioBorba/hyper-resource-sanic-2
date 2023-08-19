from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.aldeia_indigena_p import AldeiaIndigenaPResource, AldeiaIndigenaPCollectionResource

def aldeia_indigena_p_routes(app):
    
    @app.route(AldeiaIndigenaPResource.router_id())
    async def aldeia_indigena_p_id(request, id):
        r = AldeiaIndigenaPResource(request)
        return await r.get_representation(id)
    
    @app.route(AldeiaIndigenaPResource.router_id_path())
    async def aldeia_indigena_p_resource_id_path(request, id, path):
        r = AldeiaIndigenaPResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(AldeiaIndigenaPResource.router_id(), methods=['HEAD'])
    async def head_aldeia_indigena_p_id(request, id):
        r = AldeiaIndigenaPResource(request)
        return await r.head(id)
    
    @app.route(AldeiaIndigenaPResource.router_id_path(), methods=['HEAD'])
    async def head_aldeia_indigena_p_resource_id_path(request, id, path):
        r = AldeiaIndigenaPResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(AldeiaIndigenaPResource.router_id(), methods=['OPTIONS'])
    async def options_aldeia_indigena_p_id(request, id):
        r = AldeiaIndigenaPResource(request)
        return await r.options(id)
    
    @app.route(AldeiaIndigenaPResource.router_id_path(), methods=['OPTIONS'])
    async def options_aldeia_indigena_p_resource_id_path(request, id, path):
        r = AldeiaIndigenaPResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(AldeiaIndigenaPCollectionResource.router_list())
    async def aldeia_indigena_p_list(request):
        cr = AldeiaIndigenaPCollectionResource(request)
        return await cr.get_representation()
        
    @app.route(AldeiaIndigenaPCollectionResource.router_list_path())
    async def aldeia_indigena_p_list_path(request, path):
        cr = AldeiaIndigenaPCollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(AldeiaIndigenaPCollectionResource.router_list(), methods=['HEAD'] )
    async def head_aldeia_indigena_p_list(request):
        cr = AldeiaIndigenaPCollectionResource(request)
        return await cr.head()

    @app.route(AldeiaIndigenaPCollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_aldeia_indigena_p_list_path(request, path):
        cr = AldeiaIndigenaPCollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(AldeiaIndigenaPCollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_aldeia_indigena_p_list(request):
        cr = AldeiaIndigenaPCollectionResource(request)
        return await cr.options()

    @app.route(AldeiaIndigenaPCollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_aldeia_indigena_p_list_path(request, path):
        cr = AldeiaIndigenaPCollectionResource(request)
        return await cr.options_given_path(path)     
