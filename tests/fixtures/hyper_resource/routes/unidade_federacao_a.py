from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.unidade_federacao_a import UnidadeFederacaoAResource, UnidadeFederacaoACollectionResource

def unidade_federacao_a_routes(app):
    @app.route('unidade-federacao-a-list/<geocodigo:[0-9]{2}>')
    async def lim_unidade_federacao_a_geocodigo(request, geocodigo):
        r = UnidadeFederacaoAResource( request )
        return await r.get_representation( ('geocodigo', geocodigo) )


    @app.route(UnidadeFederacaoAResource.router_id())
    async def unidade_federacao_a_id(request, id):
        r = UnidadeFederacaoAResource(request)
        return await r.get_representation(id)


    @app.route('unidade-federacao-a-list/<sigla:[a-zA-Z]{2}>')
    @app.route('unidade-federacao-a-list/<sigla:[a-zA-Z]{2}>/')
    async def lim_unidade_federacao_a_sigla(request, sigla):
        r = UnidadeFederacaoAResource( request )
        return await r.get_representation( ('sigla', sigla) )

    @app.route(UnidadeFederacaoAResource.router_id_path())
    async def unidade_federacao_a_resource_id_path(request, id, path):
        r = UnidadeFederacaoAResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(UnidadeFederacaoAResource.router_id(), methods=['HEAD'])
    async def head_unidade_federacao_a_id(request, id):
        r = UnidadeFederacaoAResource(request)
        return await r.head(id)
    
    @app.route(UnidadeFederacaoAResource.router_id_path(), methods=['HEAD'])
    async def head_unidade_federacao_a_resource_id_path(request, id, path):
        r = UnidadeFederacaoAResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(UnidadeFederacaoAResource.router_id(), methods=['OPTIONS'])
    async def options_unidade_federacao_a_id(request, id):
        r = UnidadeFederacaoAResource(request)
        return await r.options(id)
    
    @app.route(UnidadeFederacaoAResource.router_id_path(), methods=['OPTIONS'])
    async def options_unidade_federacao_a_resource_id_path(request, id, path):
        r = UnidadeFederacaoAResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(UnidadeFederacaoACollectionResource.router_list())
    async def unidade_federacao_a_list(request):
        cr = UnidadeFederacaoACollectionResource(request)
        return await cr.get_representation()
        
    @app.route(UnidadeFederacaoACollectionResource.router_list_path())
    async def unidade_federacao_a_list_path(request, path):
        cr = UnidadeFederacaoACollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(UnidadeFederacaoACollectionResource.router_list(), methods=['HEAD'] )
    async def head_unidade_federacao_a_list(request):
        cr = UnidadeFederacaoACollectionResource(request)
        return await cr.head()

    @app.route(UnidadeFederacaoACollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_unidade_federacao_a_list_path(request, path):
        cr = UnidadeFederacaoACollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(UnidadeFederacaoACollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_unidade_federacao_a_list(request):
        cr = UnidadeFederacaoACollectionResource(request)
        return await cr.options()

    @app.route(UnidadeFederacaoACollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_unidade_federacao_a_list_path(request, path):
        cr = UnidadeFederacaoACollectionResource(request)
        return await cr.options_given_path(path)     
