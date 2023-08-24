from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.unidade_protecao_integral_a import UnidadeProtecaoIntegralAResource, UnidadeProtecaoIntegralACollectionResource

def unidade_protecao_integral_a_routes(app):
    
    @app.route(UnidadeProtecaoIntegralAResource.router_id())
    async def unidade_protecao_integral_a_id(request, id):
        r = UnidadeProtecaoIntegralAResource(request)
        return await r.get_representation(id)
    
    @app.route(UnidadeProtecaoIntegralAResource.router_id_path())
    async def unidade_protecao_integral_a_resource_id_path(request, id, path):
        r = UnidadeProtecaoIntegralAResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(UnidadeProtecaoIntegralAResource.router_id(), methods=['HEAD'])
    async def head_unidade_protecao_integral_a_id(request, id):
        r = UnidadeProtecaoIntegralAResource(request)
        return await r.head(id)
    
    @app.route(UnidadeProtecaoIntegralAResource.router_id_path(), methods=['HEAD'])
    async def head_unidade_protecao_integral_a_resource_id_path(request, id, path):
        r = UnidadeProtecaoIntegralAResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(UnidadeProtecaoIntegralAResource.router_id(), methods=['OPTIONS'])
    async def options_unidade_protecao_integral_a_id(request, id):
        r = UnidadeProtecaoIntegralAResource(request)
        return await r.options(id)
    
    @app.route(UnidadeProtecaoIntegralAResource.router_id_path(), methods=['OPTIONS'])
    async def options_unidade_protecao_integral_a_resource_id_path(request, id, path):
        r = UnidadeProtecaoIntegralAResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(UnidadeProtecaoIntegralACollectionResource.router_list())
    async def unidade_protecao_integral_a_list(request):
        cr = UnidadeProtecaoIntegralACollectionResource(request)
        return await cr.get_representation()
        
    @app.route(UnidadeProtecaoIntegralACollectionResource.router_list_path())
    async def unidade_protecao_integral_a_list_path(request, path):
        cr = UnidadeProtecaoIntegralACollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(UnidadeProtecaoIntegralACollectionResource.router_list(), methods=['HEAD'] )
    async def head_unidade_protecao_integral_a_list(request):
        cr = UnidadeProtecaoIntegralACollectionResource(request)
        return await cr.head()

    @app.route(UnidadeProtecaoIntegralACollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_unidade_protecao_integral_a_list_path(request, path):
        cr = UnidadeProtecaoIntegralACollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(UnidadeProtecaoIntegralACollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_unidade_protecao_integral_a_list(request):
        cr = UnidadeProtecaoIntegralACollectionResource(request)
        return await cr.options()

    @app.route(UnidadeProtecaoIntegralACollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_unidade_protecao_integral_a_list_path(request, path):
        cr = UnidadeProtecaoIntegralACollectionResource(request)
        return await cr.options_given_path(path)     
