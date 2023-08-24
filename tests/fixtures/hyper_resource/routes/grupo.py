from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.grupo import GrupoResource, GrupoCollectionResource

def grupo_routes(app):
    
    @app.route(GrupoResource.router_id())
    async def grupo_id(request, id):
        r = GrupoResource(request)
        return await r.get_representation(id)
    
    @app.route(GrupoResource.router_id_path())
    async def grupo_resource_id_path(request, id, path):
        r = GrupoResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(GrupoResource.router_id(), methods=['HEAD'])
    async def head_grupo_id(request, id):
        r = GrupoResource(request)
        return await r.head(id)
    
    @app.route(GrupoResource.router_id_path(), methods=['HEAD'])
    async def head_grupo_resource_id_path(request, id, path):
        r = GrupoResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(GrupoResource.router_id(), methods=['OPTIONS'])
    async def options_grupo_id(request, id):
        r = GrupoResource(request)
        return await r.options(id)
    
    @app.route(GrupoResource.router_id_path(), methods=['OPTIONS'])
    async def options_grupo_resource_id_path(request, id, path):
        r = GrupoResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(GrupoCollectionResource.router_list())
    async def grupo_list(request):
        cr = GrupoCollectionResource(request)
        return await cr.get_representation()
        
    @app.route(GrupoCollectionResource.router_list_path())
    async def grupo_list_path(request, path):
        cr = GrupoCollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(GrupoCollectionResource.router_list(), methods=['HEAD'] )
    async def head_grupo_list(request):
        cr = GrupoCollectionResource(request)
        return await cr.head()

    @app.route(GrupoCollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_grupo_list_path(request, path):
        cr = GrupoCollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(GrupoCollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_grupo_list(request):
        cr = GrupoCollectionResource(request)
        return await cr.options()

    @app.route(GrupoCollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_grupo_list_path(request, path):
        cr = GrupoCollectionResource(request)
        return await cr.options_given_path(path)     
