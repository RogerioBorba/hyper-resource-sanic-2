from sanic.response import json
from src.middlewares.security import authentication,permission
from src.resources.est_gerad_energia_eletrica_p import EstGeradEnergiaEletricaPResource, EstGeradEnergiaEletricaPCollectionResource

def est_gerad_energia_eletrica_p_routes(app):
    
    @app.route(EstGeradEnergiaEletricaPResource.router_id())
    async def est_gerad_energia_eletrica_p_id(request, id):
        r = EstGeradEnergiaEletricaPResource(request)
        return await r.get_representation(id)
    
    @app.route(EstGeradEnergiaEletricaPResource.router_id_path())
    async def est_gerad_energia_eletrica_p_resource_id_path(request, id, path):
        r = EstGeradEnergiaEletricaPResource(request)
        return await r.get_representation_given_path(id, path)

    @app.route(EstGeradEnergiaEletricaPResource.router_id(), methods=['HEAD'])
    async def head_est_gerad_energia_eletrica_p_id(request, id):
        r = EstGeradEnergiaEletricaPResource(request)
        return await r.head(id)
    
    @app.route(EstGeradEnergiaEletricaPResource.router_id_path(), methods=['HEAD'])
    async def head_est_gerad_energia_eletrica_p_resource_id_path(request, id, path):
        r = EstGeradEnergiaEletricaPResource(request)
        return await r.head_given_path(id, path)
    
    @app.route(EstGeradEnergiaEletricaPResource.router_id(), methods=['OPTIONS'])
    async def options_est_gerad_energia_eletrica_p_id(request, id):
        r = EstGeradEnergiaEletricaPResource(request)
        return await r.options(id)
    
    @app.route(EstGeradEnergiaEletricaPResource.router_id_path(), methods=['OPTIONS'])
    async def options_est_gerad_energia_eletrica_p_resource_id_path(request, id, path):
        r = EstGeradEnergiaEletricaPResource(request)
        return await r.options_given_path(id, path)
            
    @app.route(EstGeradEnergiaEletricaPCollectionResource.router_list())
    async def est_gerad_energia_eletrica_p_list(request):
        cr = EstGeradEnergiaEletricaPCollectionResource(request)
        return await cr.get_representation()
        
    @app.route(EstGeradEnergiaEletricaPCollectionResource.router_list_path())
    async def est_gerad_energia_eletrica_p_list_path(request, path):
        cr = EstGeradEnergiaEletricaPCollectionResource(request)
        return await cr.get_representation_given_path(path)

    @app.route(EstGeradEnergiaEletricaPCollectionResource.router_list(), methods=['HEAD'] )
    async def head_est_gerad_energia_eletrica_p_list(request):
        cr = EstGeradEnergiaEletricaPCollectionResource(request)
        return await cr.head()

    @app.route(EstGeradEnergiaEletricaPCollectionResource.router_list_path(), methods=['HEAD'] )
    async def head_est_gerad_energia_eletrica_p_list_path(request, path):
        cr = EstGeradEnergiaEletricaPCollectionResource(request)
        return await cr.head_given_path(path)
   
    @app.route(EstGeradEnergiaEletricaPCollectionResource.router_list(), methods=['OPTIONS'] )
    async def options_est_gerad_energia_eletrica_p_list(request):
        cr = EstGeradEnergiaEletricaPCollectionResource(request)
        return await cr.options()

    @app.route(EstGeradEnergiaEletricaPCollectionResource.router_list_path(), methods=['OPTIONS'] )
    async def options_est_gerad_energia_eletrica_p_list_path(request, path):
        cr = EstGeradEnergiaEletricaPCollectionResource(request)
        return await cr.options_given_path(path)     
