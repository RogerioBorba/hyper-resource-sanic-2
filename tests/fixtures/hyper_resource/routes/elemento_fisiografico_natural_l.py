from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.elemento_fisiografico_natural_l import ElementoFisiograficoNaturalLResource, ElementoFisiograficoNaturalLCollectionResource

def elemento_fisiografico_natural_l_routes(app):
    
    @app.route(ElementoFisiograficoNaturalLResource.router_id())
    async def elemento_fisiografico_natural_l_id(request, id):
        r = ElementoFisiograficoNaturalLResource(request)
        return await r.get_representation(id)
    
    @app.route(ElementoFisiograficoNaturalLResource.router_id_path())
    async def elemento_fisiografico_natural_l_resource_id_path(request, id, path):
        r = ElementoFisiograficoNaturalLResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(ElementoFisiograficoNaturalLResource.router_id(), methods=['HEAD'])
    async def head_elemento_fisiografico_natural_l_id(request, id):
        r = ElementoFisiograficoNaturalLResource(request)
        return await r.head(id)
    
    @app.route(ElementoFisiograficoNaturalLResource.router_id_path(), methods=['HEAD'])
    async def head_elemento_fisiografico_natural_l_resource_id_path(request, id, path):
        r = ElementoFisiograficoNaturalLResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(ElementoFisiograficoNaturalLResource.router_id(), methods=['OPTIONS'])
    async def options_elemento_fisiografico_natural_l_id(request, id):
        r = ElementoFisiograficoNaturalLResource(request)
        return await r.options(id)
    
    @app.route(ElementoFisiograficoNaturalLResource.router_id_path(), methods=['OPTIONS'])
    async def options_elemento_fisiografico_natural_l_resource_id_path(request, id, path):
        r = ElementoFisiograficoNaturalLResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(ElementoFisiograficoNaturalLCollectionResource.router_list())
    async def elemento_fisiografico_natural_l_list(request):
        cr = ElementoFisiograficoNaturalLCollectionResource(request)
        return await cr.get_representation()
        
    @app.route(ElementoFisiograficoNaturalLCollectionResource.router_list_path())
    async def elemento_fisiografico_natural_l_list_path(request, path):
        cr = ElementoFisiograficoNaturalLCollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(ElementoFisiograficoNaturalLCollectionResource.router_list(), methods=['HEAD'] )
    async def head_elemento_fisiografico_natural_l_list(request):
        cr = ElementoFisiograficoNaturalLCollectionResource(request)
        return await cr.head()

    @app.route(ElementoFisiograficoNaturalLCollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_elemento_fisiografico_natural_l_list_path(request, path):
        cr = ElementoFisiograficoNaturalLCollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(ElementoFisiograficoNaturalLCollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_elemento_fisiografico_natural_l_list(request):
        cr = ElementoFisiograficoNaturalLCollectionResource(request)
        return await cr.options()

    @app.route(ElementoFisiograficoNaturalLCollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_elemento_fisiografico_natural_l_list_path(request, path):
        cr = ElementoFisiograficoNaturalLCollectionResource(request)
        return await cr.options_given_path(path)     
