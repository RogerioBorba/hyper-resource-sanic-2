from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.elemento_fisiografico_natural_p import ElementoFisiograficoNaturalPResource, ElementoFisiograficoNaturalPCollectionResource

def elemento_fisiografico_natural_p_routes(app):
    
    @app.route(ElementoFisiograficoNaturalPResource.router_id())
    async def elemento_fisiografico_natural_p_id(request, id):
        r = ElementoFisiograficoNaturalPResource(request)
        return await r.get_representation(id)
    
    @app.route(ElementoFisiograficoNaturalPResource.router_id_path())
    async def elemento_fisiografico_natural_p_resource_id_path(request, id, path):
        r = ElementoFisiograficoNaturalPResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(ElementoFisiograficoNaturalPResource.router_id(), methods=['HEAD'])
    async def head_elemento_fisiografico_natural_p_id(request, id):
        r = ElementoFisiograficoNaturalPResource(request)
        return await r.head(id)
    
    @app.route(ElementoFisiograficoNaturalPResource.router_id_path(), methods=['HEAD'])
    async def head_elemento_fisiografico_natural_p_resource_id_path(request, id, path):
        r = ElementoFisiograficoNaturalPResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(ElementoFisiograficoNaturalPResource.router_id(), methods=['OPTIONS'])
    async def options_elemento_fisiografico_natural_p_id(request, id):
        r = ElementoFisiograficoNaturalPResource(request)
        return await r.options(id)
    
    @app.route(ElementoFisiograficoNaturalPResource.router_id_path(), methods=['OPTIONS'])
    async def options_elemento_fisiografico_natural_p_resource_id_path(request, id, path):
        r = ElementoFisiograficoNaturalPResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(ElementoFisiograficoNaturalPCollectionResource.router_list())
    async def elemento_fisiografico_natural_p_list(request):
        cr = ElementoFisiograficoNaturalPCollectionResource(request)
        return await cr.get_representation()
        
    @app.route(ElementoFisiograficoNaturalPCollectionResource.router_list_path())
    async def elemento_fisiografico_natural_p_list_path(request, path):
        cr = ElementoFisiograficoNaturalPCollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(ElementoFisiograficoNaturalPCollectionResource.router_list(), methods=['HEAD'] )
    async def head_elemento_fisiografico_natural_p_list(request):
        cr = ElementoFisiograficoNaturalPCollectionResource(request)
        return await cr.head()

    @app.route(ElementoFisiograficoNaturalPCollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_elemento_fisiografico_natural_p_list_path(request, path):
        cr = ElementoFisiograficoNaturalPCollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(ElementoFisiograficoNaturalPCollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_elemento_fisiografico_natural_p_list(request):
        cr = ElementoFisiograficoNaturalPCollectionResource(request)
        return await cr.options()

    @app.route(ElementoFisiograficoNaturalPCollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_elemento_fisiografico_natural_p_list_path(request, path):
        cr = ElementoFisiograficoNaturalPCollectionResource(request)
        return await cr.options_given_path(path)     
