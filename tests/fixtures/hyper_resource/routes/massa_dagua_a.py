from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.massa_dagua_a import MassaDaguaAResource, MassaDaguaACollectionResource

def massa_dagua_a_routes(app):
    
    @app.route(MassaDaguaAResource.router_id())
    async def massa_dagua_a_id(request, id):
        r = MassaDaguaAResource(request)
        return await r.get_representation(id)
    
    @app.route(MassaDaguaAResource.router_id_path())
    async def massa_dagua_a_resource_id_path(request, id, path):
        r = MassaDaguaAResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(MassaDaguaAResource.router_id(), methods=['HEAD'])
    async def head_massa_dagua_a_id(request, id):
        r = MassaDaguaAResource(request)
        return await r.head(id)
    
    @app.route(MassaDaguaAResource.router_id_path(), methods=['HEAD'])
    async def head_massa_dagua_a_resource_id_path(request, id, path):
        r = MassaDaguaAResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(MassaDaguaAResource.router_id(), methods=['OPTIONS'])
    async def options_massa_dagua_a_id(request, id):
        r = MassaDaguaAResource(request)
        return await r.options(id)
    
    @app.route(MassaDaguaAResource.router_id_path(), methods=['OPTIONS'])
    async def options_massa_dagua_a_resource_id_path(request, id, path):
        r = MassaDaguaAResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(MassaDaguaACollectionResource.router_list())
    async def massa_dagua_a_list(request):
        cr = MassaDaguaACollectionResource(request)
        return await cr.get_representation()
        
    @app.route(MassaDaguaACollectionResource.router_list_path())
    async def massa_dagua_a_list_path(request, path):
        cr = MassaDaguaACollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(MassaDaguaACollectionResource.router_list(), methods=['HEAD'] )
    async def head_massa_dagua_a_list(request):
        cr = MassaDaguaACollectionResource(request)
        return await cr.head()

    @app.route(MassaDaguaACollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_massa_dagua_a_list_path(request, path):
        cr = MassaDaguaACollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(MassaDaguaACollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_massa_dagua_a_list(request):
        cr = MassaDaguaACollectionResource(request)
        return await cr.options()

    @app.route(MassaDaguaACollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_massa_dagua_a_list_path(request, path):
        cr = MassaDaguaACollectionResource(request)
        return await cr.options_given_path(path)     
