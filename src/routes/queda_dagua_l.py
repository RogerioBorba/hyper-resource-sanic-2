from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.queda_dagua_l import QuedaDaguaLResource, QuedaDaguaLCollectionResource

def queda_dagua_l_routes(app):
    
    @app.route(QuedaDaguaLResource.router_id())
    async def queda_dagua_l_id(request, id):
        r = QuedaDaguaLResource(request)
        return await r.get_representation(id)
    
    @app.route(QuedaDaguaLResource.router_id_path())
    async def queda_dagua_l_resource_id_path(request, id, path):
        r = QuedaDaguaLResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(QuedaDaguaLResource.router_id(), methods=['HEAD'])
    async def head_queda_dagua_l_id(request, id):
        r = QuedaDaguaLResource(request)
        return await r.head(id)
    
    @app.route(QuedaDaguaLResource.router_id_path(), methods=['HEAD'])
    async def head_queda_dagua_l_resource_id_path(request, id, path):
        r = QuedaDaguaLResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(QuedaDaguaLResource.router_id(), methods=['OPTIONS'])
    async def options_queda_dagua_l_id(request, id):
        r = QuedaDaguaLResource(request)
        return await r.options(id)
    
    @app.route(QuedaDaguaLResource.router_id_path(), methods=['OPTIONS'])
    async def options_queda_dagua_l_resource_id_path(request, id, path):
        r = QuedaDaguaLResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(QuedaDaguaLCollectionResource.router_list())
    async def queda_dagua_l_list(request):
        cr = QuedaDaguaLCollectionResource(request)
        return await cr.get_representation()
        
    @app.route(QuedaDaguaLCollectionResource.router_list_path())
    async def queda_dagua_l_list_path(request, path):
        cr = QuedaDaguaLCollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(QuedaDaguaLCollectionResource.router_list(), methods=['HEAD'] )
    async def head_queda_dagua_l_list(request):
        cr = QuedaDaguaLCollectionResource(request)
        return await cr.head()

    @app.route(QuedaDaguaLCollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_queda_dagua_l_list_path(request, path):
        cr = QuedaDaguaLCollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(QuedaDaguaLCollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_queda_dagua_l_list(request):
        cr = QuedaDaguaLCollectionResource(request)
        return await cr.options()

    @app.route(QuedaDaguaLCollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_queda_dagua_l_list_path(request, path):
        cr = QuedaDaguaLCollectionResource(request)
        return await cr.options_given_path(path)     
