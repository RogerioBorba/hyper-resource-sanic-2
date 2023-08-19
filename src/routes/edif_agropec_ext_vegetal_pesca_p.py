from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.edif_agropec_ext_vegetal_pesca_p import EdifAgropecExtVegetalPescaPResource, EdifAgropecExtVegetalPescaPCollectionResource

def edif_agropec_ext_vegetal_pesca_p_routes(app):
    
    @app.route(EdifAgropecExtVegetalPescaPResource.router_id())
    async def edif_agropec_ext_vegetal_pesca_p_id(request, id):
        r = EdifAgropecExtVegetalPescaPResource(request)
        return await r.get_representation(id)
    
    @app.route(EdifAgropecExtVegetalPescaPResource.router_id_path())
    async def edif_agropec_ext_vegetal_pesca_p_resource_id_path(request, id, path):
        r = EdifAgropecExtVegetalPescaPResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(EdifAgropecExtVegetalPescaPResource.router_id(), methods=['HEAD'])
    async def head_edif_agropec_ext_vegetal_pesca_p_id(request, id):
        r = EdifAgropecExtVegetalPescaPResource(request)
        return await r.head(id)
    
    @app.route(EdifAgropecExtVegetalPescaPResource.router_id_path(), methods=['HEAD'])
    async def head_edif_agropec_ext_vegetal_pesca_p_resource_id_path(request, id, path):
        r = EdifAgropecExtVegetalPescaPResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(EdifAgropecExtVegetalPescaPResource.router_id(), methods=['OPTIONS'])
    async def options_edif_agropec_ext_vegetal_pesca_p_id(request, id):
        r = EdifAgropecExtVegetalPescaPResource(request)
        return await r.options(id)
    
    @app.route(EdifAgropecExtVegetalPescaPResource.router_id_path(), methods=['OPTIONS'])
    async def options_edif_agropec_ext_vegetal_pesca_p_resource_id_path(request, id, path):
        r = EdifAgropecExtVegetalPescaPResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(EdifAgropecExtVegetalPescaPCollectionResource.router_list())
    async def edif_agropec_ext_vegetal_pesca_p_list(request):
        cr = EdifAgropecExtVegetalPescaPCollectionResource(request)
        return await cr.get_representation()
        
    @app.route(EdifAgropecExtVegetalPescaPCollectionResource.router_list_path())
    async def edif_agropec_ext_vegetal_pesca_p_list_path(request, path):
        cr = EdifAgropecExtVegetalPescaPCollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(EdifAgropecExtVegetalPescaPCollectionResource.router_list(), methods=['HEAD'] )
    async def head_edif_agropec_ext_vegetal_pesca_p_list(request):
        cr = EdifAgropecExtVegetalPescaPCollectionResource(request)
        return await cr.head()

    @app.route(EdifAgropecExtVegetalPescaPCollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_edif_agropec_ext_vegetal_pesca_p_list_path(request, path):
        cr = EdifAgropecExtVegetalPescaPCollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(EdifAgropecExtVegetalPescaPCollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_edif_agropec_ext_vegetal_pesca_p_list(request):
        cr = EdifAgropecExtVegetalPescaPCollectionResource(request)
        return await cr.options()

    @app.route(EdifAgropecExtVegetalPescaPCollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_edif_agropec_ext_vegetal_pesca_p_list_path(request, path):
        cr = EdifAgropecExtVegetalPescaPCollectionResource(request)
        return await cr.options_given_path(path)     
