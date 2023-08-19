from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.unidade_uso_sustentavel_a import UnidadeUsoSustentavelAResource, UnidadeUsoSustentavelACollectionResource

def unidade_uso_sustentavel_a_routes(app):
    
    @app.route(UnidadeUsoSustentavelAResource.router_id())
    async def unidade_uso_sustentavel_a_id(request, id):
        r = UnidadeUsoSustentavelAResource(request)
        return await r.get_representation(id)
    
    @app.route(UnidadeUsoSustentavelAResource.router_id_path())
    async def unidade_uso_sustentavel_a_resource_id_path(request, id, path):
        r = UnidadeUsoSustentavelAResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(UnidadeUsoSustentavelAResource.router_id(), methods=['HEAD'])
    async def head_unidade_uso_sustentavel_a_id(request, id):
        r = UnidadeUsoSustentavelAResource(request)
        return await r.head(id)
    
    @app.route(UnidadeUsoSustentavelAResource.router_id_path(), methods=['HEAD'])
    async def head_unidade_uso_sustentavel_a_resource_id_path(request, id, path):
        r = UnidadeUsoSustentavelAResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(UnidadeUsoSustentavelAResource.router_id(), methods=['OPTIONS'])
    async def options_unidade_uso_sustentavel_a_id(request, id):
        r = UnidadeUsoSustentavelAResource(request)
        return await r.options(id)
    
    @app.route(UnidadeUsoSustentavelAResource.router_id_path(), methods=['OPTIONS'])
    async def options_unidade_uso_sustentavel_a_resource_id_path(request, id, path):
        r = UnidadeUsoSustentavelAResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(UnidadeUsoSustentavelACollectionResource.router_list())
    async def unidade_uso_sustentavel_a_list(request):
        cr = UnidadeUsoSustentavelACollectionResource(request)
        return await cr.get_representation()
        
    @app.route(UnidadeUsoSustentavelACollectionResource.router_list_path())
    async def unidade_uso_sustentavel_a_list_path(request, path):
        cr = UnidadeUsoSustentavelACollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(UnidadeUsoSustentavelACollectionResource.router_list(), methods=['HEAD'] )
    async def head_unidade_uso_sustentavel_a_list(request):
        cr = UnidadeUsoSustentavelACollectionResource(request)
        return await cr.head()

    @app.route(UnidadeUsoSustentavelACollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_unidade_uso_sustentavel_a_list_path(request, path):
        cr = UnidadeUsoSustentavelACollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(UnidadeUsoSustentavelACollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_unidade_uso_sustentavel_a_list(request):
        cr = UnidadeUsoSustentavelACollectionResource(request)
        return await cr.options()

    @app.route(UnidadeUsoSustentavelACollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_unidade_uso_sustentavel_a_list_path(request, path):
        cr = UnidadeUsoSustentavelACollectionResource(request)
        return await cr.options_given_path(path)     
