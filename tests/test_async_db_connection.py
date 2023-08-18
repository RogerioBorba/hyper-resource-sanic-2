import asyncio
import asyncpg
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from sqlalchemy import text
from sqlalchemy.engine.row import Row


async def main():
    # Criar um cliente para o banco de dados
    #connection = await asyncpg.connect(host="localhost",port=5432,database="postgis", user="postgres",password="desenv",)
    string_db: str = 'postgresql://postgres:desenv@127.0.0.1:5432/postgis'
    connection = await asyncpg.connect(string_db)
    print(connection)
    # Executar uma consulta
    result = await connection.fetch("SELECT * FROM public.spatial_ref_sys")

    # Iterar sobre os resultados
    for row in result:
        print(row)

    # Fechar a conexão
    await connection.close()


async def main2():
    string_db: str = 'postgresql+asyncpg://postgres:desenv@127.0.0.1:5432/postgis'
    engine:  AsyncEngine = create_async_engine(string_db,  pool_size=20, max_overflow=10)
    async with engine.connect() as conn:
        async_result = await conn.stream(text("select 'hello world' as hello") )
        async for row in async_result:
            a_row: Row =  row
            print(a_row._fields)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    #loop.run_until_complete(main())
    loop.run_until_complete(main2())
