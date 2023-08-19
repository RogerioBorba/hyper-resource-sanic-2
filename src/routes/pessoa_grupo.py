from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.pessoa_grupo import PessoaGrupoResource, PessoaGrupoCollectionResource

def pessoa_grupo_routes(app):
    
    @app.route(PessoaGrupoResource.router_id())
    async def pessoa_grupo_id(request, id):
        r = PessoaGrupoResource(request)
        return await r.get_representation(id)
    
    @app.route(PessoaGrupoResource.router_id_path())
    async def pessoa_grupo_resource_id_path(request, id, path):
        r = PessoaGrupoResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(PessoaGrupoResource.router_id(), methods=['HEAD'])
    async def head_pessoa_grupo_id(request, id):
        r = PessoaGrupoResource(request)
        return await r.head(id)
    
    @app.route(PessoaGrupoResource.router_id_path(), methods=['HEAD'])
    async def head_pessoa_grupo_resource_id_path(request, id, path):
        r = PessoaGrupoResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(PessoaGrupoResource.router_id(), methods=['OPTIONS'])
    async def options_pessoa_grupo_id(request, id):
        r = PessoaGrupoResource(request)
        return await r.options(id)
    
    @app.route(PessoaGrupoResource.router_id_path(), methods=['OPTIONS'])
    async def options_pessoa_grupo_resource_id_path(request, id, path):
        r = PessoaGrupoResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(PessoaGrupoCollectionResource.router_list())
    async def pessoa_grupo_list(request):
        cr = PessoaGrupoCollectionResource(request)
        return await cr.get_representation()
        
    @app.route(PessoaGrupoCollectionResource.router_list_path())
    async def pessoa_grupo_list_path(request, path):
        cr = PessoaGrupoCollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(PessoaGrupoCollectionResource.router_list(), methods=['HEAD'] )
    async def head_pessoa_grupo_list(request):
        cr = PessoaGrupoCollectionResource(request)
        return await cr.head()

    @app.route(PessoaGrupoCollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_pessoa_grupo_list_path(request, path):
        cr = PessoaGrupoCollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(PessoaGrupoCollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_pessoa_grupo_list(request):
        cr = PessoaGrupoCollectionResource(request)
        return await cr.options()

    @app.route(PessoaGrupoCollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_pessoa_grupo_list_path(request, path):
        cr = PessoaGrupoCollectionResource(request)
        return await cr.options_given_path(path)     
