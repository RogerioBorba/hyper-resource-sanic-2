from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.termeletrica_p import TermeletricaPResource, TermeletricaPCollectionResource

def termeletrica_p_routes(app):
    
    @app.route(TermeletricaPResource.router_id())
    async def termeletrica_p_id(request, id):
        r = TermeletricaPResource(request)
        return await r.get_representation(id)
    
    @app.route(TermeletricaPResource.router_id_path())
    async def termeletrica_p_resource_id_path(request, id, path):
        r = TermeletricaPResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(TermeletricaPResource.router_id(), methods=['HEAD'])
    async def head_termeletrica_p_id(request, id):
        r = TermeletricaPResource(request)
        return await r.head(id)
    
    @app.route(TermeletricaPResource.router_id_path(), methods=['HEAD'])
    async def head_termeletrica_p_resource_id_path(request, id, path):
        r = TermeletricaPResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(TermeletricaPResource.router_id(), methods=['OPTIONS'])
    async def options_termeletrica_p_id(request, id):
        r = TermeletricaPResource(request)
        return await r.options(id)
    
    @app.route(TermeletricaPResource.router_id_path(), methods=['OPTIONS'])
    async def options_termeletrica_p_resource_id_path(request, id, path):
        r = TermeletricaPResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(TermeletricaPCollectionResource.router_list())
    async def termeletrica_p_list(request):
        cr = TermeletricaPCollectionResource(request)
        return await cr.get_representation()
        
    @app.route(TermeletricaPCollectionResource.router_list_path())
    async def termeletrica_p_list_path(request, path):
        cr = TermeletricaPCollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(TermeletricaPCollectionResource.router_list(), methods=['HEAD'] )
    async def head_termeletrica_p_list(request):
        cr = TermeletricaPCollectionResource(request)
        return await cr.head()

    @app.route(TermeletricaPCollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_termeletrica_p_list_path(request, path):
        cr = TermeletricaPCollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(TermeletricaPCollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_termeletrica_p_list(request):
        cr = TermeletricaPCollectionResource(request)
        return await cr.options()

    @app.route(TermeletricaPCollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_termeletrica_p_list_path(request, path):
        cr = TermeletricaPCollectionResource(request)
        return await cr.options_given_path(path)     
