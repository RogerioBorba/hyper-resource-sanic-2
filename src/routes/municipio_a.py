from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.municipio_a import MunicipioAResource, MunicipioACollectionResource

def municipio_a_routes(app):
    
    @app.route(MunicipioAResource.router_id())
    async def municipio_a_id(request, id):
        r = MunicipioAResource(request)
        return await r.get_representation(id)
    
    @app.route(MunicipioAResource.router_id_path())
    async def municipio_a_resource_id_path(request, id, path):
        r = MunicipioAResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(MunicipioAResource.router_id(), methods=['HEAD'])
    async def head_municipio_a_id(request, id):
        r = MunicipioAResource(request)
        return await r.head(id)
    
    @app.route(MunicipioAResource.router_id_path(), methods=['HEAD'])
    async def head_municipio_a_resource_id_path(request, id, path):
        r = MunicipioAResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(MunicipioAResource.router_id(), methods=['OPTIONS'])
    async def options_municipio_a_id(request, id):
        r = MunicipioAResource(request)
        return await r.options(id)
    
    @app.route(MunicipioAResource.router_id_path(), methods=['OPTIONS'])
    async def options_municipio_a_resource_id_path(request, id, path):
        r = MunicipioAResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(MunicipioACollectionResource.router_list())
    async def municipio_a_list(request):
        cr = MunicipioACollectionResource(request)
        return await cr.get_representation()
        
    @app.route(MunicipioACollectionResource.router_list_path())
    async def municipio_a_list_path(request, path):
        cr = MunicipioACollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(MunicipioACollectionResource.router_list(), methods=['HEAD'] )
    async def head_municipio_a_list(request):
        cr = MunicipioACollectionResource(request)
        return await cr.head()

    @app.route(MunicipioACollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_municipio_a_list_path(request, path):
        cr = MunicipioACollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(MunicipioACollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_municipio_a_list(request):
        cr = MunicipioACollectionResource(request)
        return await cr.options()

    @app.route(MunicipioACollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_municipio_a_list_path(request, path):
        cr = MunicipioACollectionResource(request)
        return await cr.options_given_path(path)     
