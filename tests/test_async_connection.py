import asyncio
import aiohttp
from aiohttp import ClientSession


async def test_get_request(session: ClientSession, url: str):
    response = await session.get(url)
    assert response.status == 200

async def main():
    session = aiohttp.ClientSession()
    await test_get_request(session, "https://www.google.com")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())