from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.terreno_sujeito_inundacao_a import TerrenoSujeitoInundacaoAResource, TerrenoSujeitoInundacaoACollectionResource

def terreno_sujeito_inundacao_a_routes(app):
    
    @app.route(TerrenoSujeitoInundacaoAResource.router_id())
    async def terreno_sujeito_inundacao_a_id(request, id):
        r = TerrenoSujeitoInundacaoAResource(request)
        return await r.get_representation(id)
    
    @app.route(TerrenoSujeitoInundacaoAResource.router_id_path())
    async def terreno_sujeito_inundacao_a_resource_id_path(request, id, path):
        r = TerrenoSujeitoInundacaoAResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(TerrenoSujeitoInundacaoAResource.router_id(), methods=['HEAD'])
    async def head_terreno_sujeito_inundacao_a_id(request, id):
        r = TerrenoSujeitoInundacaoAResource(request)
        return await r.head(id)
    
    @app.route(TerrenoSujeitoInundacaoAResource.router_id_path(), methods=['HEAD'])
    async def head_terreno_sujeito_inundacao_a_resource_id_path(request, id, path):
        r = TerrenoSujeitoInundacaoAResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(TerrenoSujeitoInundacaoAResource.router_id(), methods=['OPTIONS'])
    async def options_terreno_sujeito_inundacao_a_id(request, id):
        r = TerrenoSujeitoInundacaoAResource(request)
        return await r.options(id)
    
    @app.route(TerrenoSujeitoInundacaoAResource.router_id_path(), methods=['OPTIONS'])
    async def options_terreno_sujeito_inundacao_a_resource_id_path(request, id, path):
        r = TerrenoSujeitoInundacaoAResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(TerrenoSujeitoInundacaoACollectionResource.router_list())
    async def terreno_sujeito_inundacao_a_list(request):
        cr = TerrenoSujeitoInundacaoACollectionResource(request)
        return await cr.get_representation()
        
    @app.route(TerrenoSujeitoInundacaoACollectionResource.router_list_path())
    async def terreno_sujeito_inundacao_a_list_path(request, path):
        cr = TerrenoSujeitoInundacaoACollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(TerrenoSujeitoInundacaoACollectionResource.router_list(), methods=['HEAD'] )
    async def head_terreno_sujeito_inundacao_a_list(request):
        cr = TerrenoSujeitoInundacaoACollectionResource(request)
        return await cr.head()

    @app.route(TerrenoSujeitoInundacaoACollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_terreno_sujeito_inundacao_a_list_path(request, path):
        cr = TerrenoSujeitoInundacaoACollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(TerrenoSujeitoInundacaoACollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_terreno_sujeito_inundacao_a_list(request):
        cr = TerrenoSujeitoInundacaoACollectionResource(request)
        return await cr.options()

    @app.route(TerrenoSujeitoInundacaoACollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_terreno_sujeito_inundacao_a_list_path(request, path):
        cr = TerrenoSujeitoInundacaoACollectionResource(request)
        return await cr.options_given_path(path)     
