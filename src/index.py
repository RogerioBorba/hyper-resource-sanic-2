import aiohttp
from sanic import Sanic, response
from sanic.request import Request
from sanic.response import text, json
from environs import Env

from src.aiohttp_client import ClientIOHTTP
from src.orm.database_postgresql import DialectDbPostgresql
from src.resources.setup_resources import setup_all_resources
from src.routes.entry_point import api_entry_point
from src.routes.setup_routes import setup_all_routes
# Create Sanic app
app = Sanic(__name__)

# Setup env
env = Env()
env.read_env()  # read .env file, if it exists
port: int = env.int("PORT", 8002)
host: str = env.str("HOST", "127.0.0.1")
debug: bool =env.bool("DEBUG", False)
access_log: bool = env.bool("ACESS_LOG", False)


# Setup all routes
setup_all_routes(app)
@app.get("/routes")
async def list_routes(request):

    for r in list(app.router.routes_all.values()):
        print(r)
    #print(list(routes.values())[0].handler.__name__)
    #return text("texto")
    routes = []
    for route in list(app.router.routes_all.values()):
        routes.append({
            "uri": route.path,
            #"methods": list(route.methods),
            "handler": route.name,
        })
    return json(routes)


@app.listener("after_server_start")
async def init_session(app, loop):
    print('after_server_start')
    app.ctx.aiohttp_session = aiohttp.ClientSession(loop=loop)
    ClientIOHTTP().set_session(app.ctx.aiohttp_session) #aiohttp.ClientSession(loop=loop)  # app.aiohttp_session
    print("Initializing ClientIOHTTP ...")
    print(ClientIOHTTP().session)



@app.route("/", methods=["GET"])
def handle_request(request: Request):
    base_iri = request.scheme + '://' + request.host
    _headers = {'Access-Control-Expose-Headers': 'Link', 'Link': f'<{base_iri}>;rel=https://schema.org/EntryPoint'}
    print(_headers)
    print("GET and OPTIONS")
    # return response.json(api_entry_point())
    return response.json( api_entry_point(), headers=_headers, status=200 )


@app.listener("after_server_start")
async def connect_to_db(*args, **kwargs):
    if env.bool("HAS_DATABASE", False):
        from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
        print("after_server_start initialize Database")
        engine: AsyncEngine = create_async_engine(env.str("ASYNC_URLDB"), echo=env.bool("DEBUG", False))
        app.ctx.engine = engine
        app.ctx.dialect_db_class = DialectDbPostgresql
        app.ctx.db = engine

if __name__ == "__main__":
    print(f"Starting server at port: {port}")
    #setup_all_resources()
    app.run(host=host, port=port, debug=True, access_log=True, auto_reload=True)
