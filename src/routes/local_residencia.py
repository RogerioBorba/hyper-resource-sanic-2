from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.local_residencia import LocalResidenciaResource, LocalResidenciaCollectionResource

def local_residencia_routes(app):
    
    @app.route(LocalResidenciaResource.router_id())
    async def local_residencia_id(request, id):
        r = LocalResidenciaResource(request)
        return await r.get_representation(id)
    
    @app.route(LocalResidenciaResource.router_id_path())
    async def local_residencia_resource_id_path(request, id, path):
        r = LocalResidenciaResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(LocalResidenciaResource.router_id(), methods=['HEAD'])
    async def head_local_residencia_id(request, id):
        r = LocalResidenciaResource(request)
        return await r.head(id)
    
    @app.route(LocalResidenciaResource.router_id_path(), methods=['HEAD'])
    async def head_local_residencia_resource_id_path(request, id, path):
        r = LocalResidenciaResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(LocalResidenciaResource.router_id(), methods=['OPTIONS'])
    async def options_local_residencia_id(request, id):
        r = LocalResidenciaResource(request)
        return await r.options(id)
    
    @app.route(LocalResidenciaResource.router_id_path(), methods=['OPTIONS'])
    async def options_local_residencia_resource_id_path(request, id, path):
        r = LocalResidenciaResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(LocalResidenciaCollectionResource.router_list())
    async def local_residencia_list(request):
        cr = LocalResidenciaCollectionResource(request)
        return await cr.get_representation()
        
    @app.route(LocalResidenciaCollectionResource.router_list_path())
    async def local_residencia_list_path(request, path):
        cr = LocalResidenciaCollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(LocalResidenciaCollectionResource.router_list(), methods=['HEAD'] )
    async def head_local_residencia_list(request):
        cr = LocalResidenciaCollectionResource(request)
        return await cr.head()

    @app.route(LocalResidenciaCollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_local_residencia_list_path(request, path):
        cr = LocalResidenciaCollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(LocalResidenciaCollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_local_residencia_list(request):
        cr = LocalResidenciaCollectionResource(request)
        return await cr.options()

    @app.route(LocalResidenciaCollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_local_residencia_list_path(request, path):
        cr = LocalResidenciaCollectionResource(request)
        return await cr.options_given_path(path)     
