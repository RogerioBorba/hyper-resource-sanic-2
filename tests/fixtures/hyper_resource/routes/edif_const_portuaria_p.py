from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.edif_const_portuaria_p import EdifConstPortuariaPResource, EdifConstPortuariaPCollectionResource

def edif_const_portuaria_p_routes(app):
    
    @app.route(EdifConstPortuariaPResource.router_id())
    async def edif_const_portuaria_p_id(request, id):
        r = EdifConstPortuariaPResource(request)
        return await r.get_representation(id)
    
    @app.route(EdifConstPortuariaPResource.router_id_path())
    async def edif_const_portuaria_p_resource_id_path(request, id, path):
        r = EdifConstPortuariaPResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(EdifConstPortuariaPResource.router_id(), methods=['HEAD'])
    async def head_edif_const_portuaria_p_id(request, id):
        r = EdifConstPortuariaPResource(request)
        return await r.head(id)
    
    @app.route(EdifConstPortuariaPResource.router_id_path(), methods=['HEAD'])
    async def head_edif_const_portuaria_p_resource_id_path(request, id, path):
        r = EdifConstPortuariaPResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(EdifConstPortuariaPResource.router_id(), methods=['OPTIONS'])
    async def options_edif_const_portuaria_p_id(request, id):
        r = EdifConstPortuariaPResource(request)
        return await r.options(id)
    
    @app.route(EdifConstPortuariaPResource.router_id_path(), methods=['OPTIONS'])
    async def options_edif_const_portuaria_p_resource_id_path(request, id, path):
        r = EdifConstPortuariaPResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(EdifConstPortuariaPCollectionResource.router_list())
    async def edif_const_portuaria_p_list(request):
        cr = EdifConstPortuariaPCollectionResource(request)
        return await cr.get_representation()
        
    @app.route(EdifConstPortuariaPCollectionResource.router_list_path())
    async def edif_const_portuaria_p_list_path(request, path):
        cr = EdifConstPortuariaPCollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(EdifConstPortuariaPCollectionResource.router_list(), methods=['HEAD'] )
    async def head_edif_const_portuaria_p_list(request):
        cr = EdifConstPortuariaPCollectionResource(request)
        return await cr.head()

    @app.route(EdifConstPortuariaPCollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_edif_const_portuaria_p_list_path(request, path):
        cr = EdifConstPortuariaPCollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(EdifConstPortuariaPCollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_edif_const_portuaria_p_list(request):
        cr = EdifConstPortuariaPCollectionResource(request)
        return await cr.options()

    @app.route(EdifConstPortuariaPCollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_edif_const_portuaria_p_list_path(request, path):
        cr = EdifConstPortuariaPCollectionResource(request)
        return await cr.options_given_path(path)     
