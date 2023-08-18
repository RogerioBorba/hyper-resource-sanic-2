from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.mangue_a import MangueAResource, MangueACollectionResource

def mangue_a_routes(app):
    
    @app.route(MangueAResource.router_id())
    async def mangue_a_id(request, id):
        r = MangueAResource(request)
        return await r.get_representation(id)
    
    @app.route(MangueAResource.router_id_path())
    async def mangue_a_resource_id_path(request, id, path):
        r = MangueAResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(MangueAResource.router_id(), methods=['HEAD'])
    async def head_mangue_a_id(request, id):
        r = MangueAResource(request)
        return await r.head(id)
    
    @app.route(MangueAResource.router_id_path(), methods=['HEAD'])
    async def head_mangue_a_resource_id_path(request, id, path):
        r = MangueAResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(MangueAResource.router_id(), methods=['OPTIONS'])
    async def options_mangue_a_id(request, id):
        r = MangueAResource(request)
        return await r.options(id)
    
    @app.route(MangueAResource.router_id_path(), methods=['OPTIONS'])
    async def options_mangue_a_resource_id_path(request, id, path):
        r = MangueAResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(MangueACollectionResource.router_list())
    async def mangue_a_list(request):
        cr = MangueACollectionResource(request)
        return await cr.get_representation()
        
    @app.route(MangueACollectionResource.router_list_path())
    async def mangue_a_list_path(request, path):
        cr = MangueACollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(MangueACollectionResource.router_list(), methods=['HEAD'] )
    async def head_mangue_a_list(request):
        cr = MangueACollectionResource(request)
        return await cr.head()

    @app.route(MangueACollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_mangue_a_list_path(request, path):
        cr = MangueACollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(MangueACollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_mangue_a_list(request):
        cr = MangueACollectionResource(request)
        return await cr.options()

    @app.route(MangueACollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_mangue_a_list_path(request, path):
        cr = MangueACollectionResource(request)
        return await cr.options_given_path(path)     
