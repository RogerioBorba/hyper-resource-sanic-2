from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.trecho_massa_dagua_a import TrechoMassaDaguaAResource, TrechoMassaDaguaACollectionResource

def trecho_massa_dagua_a_routes(app):
    
    @app.route(TrechoMassaDaguaAResource.router_id())
    async def trecho_massa_dagua_a_id(request, id):
        r = TrechoMassaDaguaAResource(request)
        return await r.get_representation(id)
    
    @app.route(TrechoMassaDaguaAResource.router_id_path())
    async def trecho_massa_dagua_a_resource_id_path(request, id, path):
        r = TrechoMassaDaguaAResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(TrechoMassaDaguaAResource.router_id(), methods=['HEAD'])
    async def head_trecho_massa_dagua_a_id(request, id):
        r = TrechoMassaDaguaAResource(request)
        return await r.head(id)
    
    @app.route(TrechoMassaDaguaAResource.router_id_path(), methods=['HEAD'])
    async def head_trecho_massa_dagua_a_resource_id_path(request, id, path):
        r = TrechoMassaDaguaAResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(TrechoMassaDaguaAResource.router_id(), methods=['OPTIONS'])
    async def options_trecho_massa_dagua_a_id(request, id):
        r = TrechoMassaDaguaAResource(request)
        return await r.options(id)
    
    @app.route(TrechoMassaDaguaAResource.router_id_path(), methods=['OPTIONS'])
    async def options_trecho_massa_dagua_a_resource_id_path(request, id, path):
        r = TrechoMassaDaguaAResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(TrechoMassaDaguaACollectionResource.router_list())
    async def trecho_massa_dagua_a_list(request):
        cr = TrechoMassaDaguaACollectionResource(request)
        return await cr.get_representation()
        
    @app.route(TrechoMassaDaguaACollectionResource.router_list_path())
    async def trecho_massa_dagua_a_list_path(request, path):
        cr = TrechoMassaDaguaACollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(TrechoMassaDaguaACollectionResource.router_list(), methods=['HEAD'] )
    async def head_trecho_massa_dagua_a_list(request):
        cr = TrechoMassaDaguaACollectionResource(request)
        return await cr.head()

    @app.route(TrechoMassaDaguaACollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_trecho_massa_dagua_a_list_path(request, path):
        cr = TrechoMassaDaguaACollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(TrechoMassaDaguaACollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_trecho_massa_dagua_a_list(request):
        cr = TrechoMassaDaguaACollectionResource(request)
        return await cr.options()

    @app.route(TrechoMassaDaguaACollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_trecho_massa_dagua_a_list_path(request, path):
        cr = TrechoMassaDaguaACollectionResource(request)
        return await cr.options_given_path(path)     
