from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.edif_metro_ferroviaria_p import EdifMetroFerroviariaPResource, EdifMetroFerroviariaPCollectionResource

def edif_metro_ferroviaria_p_routes(app):
    
    @app.route(EdifMetroFerroviariaPResource.router_id())
    async def edif_metro_ferroviaria_p_id(request, id):
        r = EdifMetroFerroviariaPResource(request)
        return await r.get_representation(id)
    
    @app.route(EdifMetroFerroviariaPResource.router_id_path())
    async def edif_metro_ferroviaria_p_resource_id_path(request, id, path):
        r = EdifMetroFerroviariaPResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(EdifMetroFerroviariaPResource.router_id(), methods=['HEAD'])
    async def head_edif_metro_ferroviaria_p_id(request, id):
        r = EdifMetroFerroviariaPResource(request)
        return await r.head(id)
    
    @app.route(EdifMetroFerroviariaPResource.router_id_path(), methods=['HEAD'])
    async def head_edif_metro_ferroviaria_p_resource_id_path(request, id, path):
        r = EdifMetroFerroviariaPResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(EdifMetroFerroviariaPResource.router_id(), methods=['OPTIONS'])
    async def options_edif_metro_ferroviaria_p_id(request, id):
        r = EdifMetroFerroviariaPResource(request)
        return await r.options(id)
    
    @app.route(EdifMetroFerroviariaPResource.router_id_path(), methods=['OPTIONS'])
    async def options_edif_metro_ferroviaria_p_resource_id_path(request, id, path):
        r = EdifMetroFerroviariaPResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(EdifMetroFerroviariaPCollectionResource.router_list())
    async def edif_metro_ferroviaria_p_list(request):
        cr = EdifMetroFerroviariaPCollectionResource(request)
        return await cr.get_representation()
        
    @app.route(EdifMetroFerroviariaPCollectionResource.router_list_path())
    async def edif_metro_ferroviaria_p_list_path(request, path):
        cr = EdifMetroFerroviariaPCollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(EdifMetroFerroviariaPCollectionResource.router_list(), methods=['HEAD'] )
    async def head_edif_metro_ferroviaria_p_list(request):
        cr = EdifMetroFerroviariaPCollectionResource(request)
        return await cr.head()

    @app.route(EdifMetroFerroviariaPCollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_edif_metro_ferroviaria_p_list_path(request, path):
        cr = EdifMetroFerroviariaPCollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(EdifMetroFerroviariaPCollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_edif_metro_ferroviaria_p_list(request):
        cr = EdifMetroFerroviariaPCollectionResource(request)
        return await cr.options()

    @app.route(EdifMetroFerroviariaPCollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_edif_metro_ferroviaria_p_list_path(request, path):
        cr = EdifMetroFerroviariaPCollectionResource(request)
        return await cr.options_given_path(path)     
