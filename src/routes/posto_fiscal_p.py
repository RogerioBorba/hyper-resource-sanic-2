from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.posto_fiscal_p import PostoFiscalPResource, PostoFiscalPCollectionResource

def posto_fiscal_p_routes(app):
    
    @app.route(PostoFiscalPResource.router_id())
    async def posto_fiscal_p_id(request, id):
        r = PostoFiscalPResource(request)
        return await r.get_representation(id)
    
    @app.route(PostoFiscalPResource.router_id_path())
    async def posto_fiscal_p_resource_id_path(request, id, path):
        r = PostoFiscalPResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(PostoFiscalPResource.router_id(), methods=['HEAD'])
    async def head_posto_fiscal_p_id(request, id):
        r = PostoFiscalPResource(request)
        return await r.head(id)
    
    @app.route(PostoFiscalPResource.router_id_path(), methods=['HEAD'])
    async def head_posto_fiscal_p_resource_id_path(request, id, path):
        r = PostoFiscalPResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(PostoFiscalPResource.router_id(), methods=['OPTIONS'])
    async def options_posto_fiscal_p_id(request, id):
        r = PostoFiscalPResource(request)
        return await r.options(id)
    
    @app.route(PostoFiscalPResource.router_id_path(), methods=['OPTIONS'])
    async def options_posto_fiscal_p_resource_id_path(request, id, path):
        r = PostoFiscalPResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(PostoFiscalPCollectionResource.router_list())
    async def posto_fiscal_p_list(request):
        cr = PostoFiscalPCollectionResource(request)
        return await cr.get_representation()
        
    @app.route(PostoFiscalPCollectionResource.router_list_path())
    async def posto_fiscal_p_list_path(request, path):
        cr = PostoFiscalPCollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(PostoFiscalPCollectionResource.router_list(), methods=['HEAD'] )
    async def head_posto_fiscal_p_list(request):
        cr = PostoFiscalPCollectionResource(request)
        return await cr.head()

    @app.route(PostoFiscalPCollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_posto_fiscal_p_list_path(request, path):
        cr = PostoFiscalPCollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(PostoFiscalPCollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_posto_fiscal_p_list(request):
        cr = PostoFiscalPCollectionResource(request)
        return await cr.options()

    @app.route(PostoFiscalPCollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_posto_fiscal_p_list_path(request, path):
        cr = PostoFiscalPCollectionResource(request)
        return await cr.options_given_path(path)     
