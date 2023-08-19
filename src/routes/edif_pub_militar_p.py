from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.edif_pub_militar_p import EdifPubMilitarPResource, EdifPubMilitarPCollectionResource

def edif_pub_militar_p_routes(app):
    
    @app.route(EdifPubMilitarPResource.router_id())
    async def edif_pub_militar_p_id(request, id):
        r = EdifPubMilitarPResource(request)
        return await r.get_representation(id)
    
    @app.route(EdifPubMilitarPResource.router_id_path())
    async def edif_pub_militar_p_resource_id_path(request, id, path):
        r = EdifPubMilitarPResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(EdifPubMilitarPResource.router_id(), methods=['HEAD'])
    async def head_edif_pub_militar_p_id(request, id):
        r = EdifPubMilitarPResource(request)
        return await r.head(id)
    
    @app.route(EdifPubMilitarPResource.router_id_path(), methods=['HEAD'])
    async def head_edif_pub_militar_p_resource_id_path(request, id, path):
        r = EdifPubMilitarPResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(EdifPubMilitarPResource.router_id(), methods=['OPTIONS'])
    async def options_edif_pub_militar_p_id(request, id):
        r = EdifPubMilitarPResource(request)
        return await r.options(id)
    
    @app.route(EdifPubMilitarPResource.router_id_path(), methods=['OPTIONS'])
    async def options_edif_pub_militar_p_resource_id_path(request, id, path):
        r = EdifPubMilitarPResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(EdifPubMilitarPCollectionResource.router_list())
    async def edif_pub_militar_p_list(request):
        cr = EdifPubMilitarPCollectionResource(request)
        return await cr.get_representation()
        
    @app.route(EdifPubMilitarPCollectionResource.router_list_path())
    async def edif_pub_militar_p_list_path(request, path):
        cr = EdifPubMilitarPCollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(EdifPubMilitarPCollectionResource.router_list(), methods=['HEAD'] )
    async def head_edif_pub_militar_p_list(request):
        cr = EdifPubMilitarPCollectionResource(request)
        return await cr.head()

    @app.route(EdifPubMilitarPCollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_edif_pub_militar_p_list_path(request, path):
        cr = EdifPubMilitarPCollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(EdifPubMilitarPCollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_edif_pub_militar_p_list(request):
        cr = EdifPubMilitarPCollectionResource(request)
        return await cr.options()

    @app.route(EdifPubMilitarPCollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_edif_pub_militar_p_list_path(request, path):
        cr = EdifPubMilitarPCollectionResource(request)
        return await cr.options_given_path(path)     
