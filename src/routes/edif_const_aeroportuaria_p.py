from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.edif_const_aeroportuaria_p import EdifConstAeroportuariaPResource, EdifConstAeroportuariaPCollectionResource

def edif_const_aeroportuaria_p_routes(app):
    
    @app.route(EdifConstAeroportuariaPResource.router_id())
    async def edif_const_aeroportuaria_p_id(request, id):
        r = EdifConstAeroportuariaPResource(request)
        return await r.get_representation(id)
    
    @app.route(EdifConstAeroportuariaPResource.router_id_path())
    async def edif_const_aeroportuaria_p_resource_id_path(request, id, path):
        r = EdifConstAeroportuariaPResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(EdifConstAeroportuariaPResource.router_id(), methods=['HEAD'])
    async def head_edif_const_aeroportuaria_p_id(request, id):
        r = EdifConstAeroportuariaPResource(request)
        return await r.head(id)
    
    @app.route(EdifConstAeroportuariaPResource.router_id_path(), methods=['HEAD'])
    async def head_edif_const_aeroportuaria_p_resource_id_path(request, id, path):
        r = EdifConstAeroportuariaPResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(EdifConstAeroportuariaPResource.router_id(), methods=['OPTIONS'])
    async def options_edif_const_aeroportuaria_p_id(request, id):
        r = EdifConstAeroportuariaPResource(request)
        return await r.options(id)
    
    @app.route(EdifConstAeroportuariaPResource.router_id_path(), methods=['OPTIONS'])
    async def options_edif_const_aeroportuaria_p_resource_id_path(request, id, path):
        r = EdifConstAeroportuariaPResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(EdifConstAeroportuariaPCollectionResource.router_list())
    async def edif_const_aeroportuaria_p_list(request):
        cr = EdifConstAeroportuariaPCollectionResource(request)
        return await cr.get_representation()
        
    @app.route(EdifConstAeroportuariaPCollectionResource.router_list_path())
    async def edif_const_aeroportuaria_p_list_path(request, path):
        cr = EdifConstAeroportuariaPCollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(EdifConstAeroportuariaPCollectionResource.router_list(), methods=['HEAD'] )
    async def head_edif_const_aeroportuaria_p_list(request):
        cr = EdifConstAeroportuariaPCollectionResource(request)
        return await cr.head()

    @app.route(EdifConstAeroportuariaPCollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_edif_const_aeroportuaria_p_list_path(request, path):
        cr = EdifConstAeroportuariaPCollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(EdifConstAeroportuariaPCollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_edif_const_aeroportuaria_p_list(request):
        cr = EdifConstAeroportuariaPCollectionResource(request)
        return await cr.options()

    @app.route(EdifConstAeroportuariaPCollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_edif_const_aeroportuaria_p_list_path(request, path):
        cr = EdifConstAeroportuariaPCollectionResource(request)
        return await cr.options_given_path(path)     
