from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.unidade_conservacao_nao_snuc_a import UnidadeConservacaoNaoSnucAResource, UnidadeConservacaoNaoSnucACollectionResource

def unidade_conservacao_nao_snuc_a_routes(app):
    
    @app.route(UnidadeConservacaoNaoSnucAResource.router_id())
    async def unidade_conservacao_nao_snuc_a_id(request, id):
        r = UnidadeConservacaoNaoSnucAResource(request)
        return await r.get_representation(id)
    
    @app.route(UnidadeConservacaoNaoSnucAResource.router_id_path())
    async def unidade_conservacao_nao_snuc_a_resource_id_path(request, id, path):
        r = UnidadeConservacaoNaoSnucAResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(UnidadeConservacaoNaoSnucAResource.router_id(), methods=['HEAD'])
    async def head_unidade_conservacao_nao_snuc_a_id(request, id):
        r = UnidadeConservacaoNaoSnucAResource(request)
        return await r.head(id)
    
    @app.route(UnidadeConservacaoNaoSnucAResource.router_id_path(), methods=['HEAD'])
    async def head_unidade_conservacao_nao_snuc_a_resource_id_path(request, id, path):
        r = UnidadeConservacaoNaoSnucAResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(UnidadeConservacaoNaoSnucAResource.router_id(), methods=['OPTIONS'])
    async def options_unidade_conservacao_nao_snuc_a_id(request, id):
        r = UnidadeConservacaoNaoSnucAResource(request)
        return await r.options(id)
    
    @app.route(UnidadeConservacaoNaoSnucAResource.router_id_path(), methods=['OPTIONS'])
    async def options_unidade_conservacao_nao_snuc_a_resource_id_path(request, id, path):
        r = UnidadeConservacaoNaoSnucAResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(UnidadeConservacaoNaoSnucACollectionResource.router_list())
    async def unidade_conservacao_nao_snuc_a_list(request):
        cr = UnidadeConservacaoNaoSnucACollectionResource(request)
        return await cr.get_representation()
        
    @app.route(UnidadeConservacaoNaoSnucACollectionResource.router_list_path())
    async def unidade_conservacao_nao_snuc_a_list_path(request, path):
        cr = UnidadeConservacaoNaoSnucACollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(UnidadeConservacaoNaoSnucACollectionResource.router_list(), methods=['HEAD'] )
    async def head_unidade_conservacao_nao_snuc_a_list(request):
        cr = UnidadeConservacaoNaoSnucACollectionResource(request)
        return await cr.head()

    @app.route(UnidadeConservacaoNaoSnucACollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_unidade_conservacao_nao_snuc_a_list_path(request, path):
        cr = UnidadeConservacaoNaoSnucACollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(UnidadeConservacaoNaoSnucACollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_unidade_conservacao_nao_snuc_a_list(request):
        cr = UnidadeConservacaoNaoSnucACollectionResource(request)
        return await cr.options()

    @app.route(UnidadeConservacaoNaoSnucACollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_unidade_conservacao_nao_snuc_a_list_path(request, path):
        cr = UnidadeConservacaoNaoSnucACollectionResource(request)
        return await cr.options_given_path(path)     
