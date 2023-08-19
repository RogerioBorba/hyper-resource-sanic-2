from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.pessoa import PessoaResource, PessoaCollectionResource

def pessoa_routes(app):
    
    @app.route(PessoaResource.router_id())
    async def pessoa_id(request, id):
        r = PessoaResource(request)
        return await r.get_representation(id)
    
    @app.route(PessoaResource.router_id_path())
    async def pessoa_resource_id_path(request, id, path):
        r = PessoaResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(PessoaResource.router_id(), methods=['HEAD'])
    async def head_pessoa_id(request, id):
        r = PessoaResource(request)
        return await r.head(id)
    
    @app.route(PessoaResource.router_id_path(), methods=['HEAD'])
    async def head_pessoa_resource_id_path(request, id, path):
        r = PessoaResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(PessoaResource.router_id(), methods=['OPTIONS'])
    async def options_pessoa_id(request, id):
        r = PessoaResource(request)
        return await r.options(id)
    
    @app.route(PessoaResource.router_id_path(), methods=['OPTIONS'])
    async def options_pessoa_resource_id_path(request, id, path):
        r = PessoaResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(PessoaCollectionResource.router_list())
    async def pessoa_list(request):
        cr = PessoaCollectionResource(request)
        return await cr.get_representation()
        
    @app.route(PessoaCollectionResource.router_list_path())
    async def pessoa_list_path(request, path):
        cr = PessoaCollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(PessoaCollectionResource.router_list(), methods=['HEAD'] )
    async def head_pessoa_list(request):
        cr = PessoaCollectionResource(request)
        return await cr.head()

    @app.route(PessoaCollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_pessoa_list_path(request, path):
        cr = PessoaCollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(PessoaCollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_pessoa_list(request):
        cr = PessoaCollectionResource(request)
        return await cr.options()

    @app.route(PessoaCollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_pessoa_list_path(request, path):
        cr = PessoaCollectionResource(request)
        return await cr.options_given_path(path)     
