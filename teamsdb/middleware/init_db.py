from aiohttp.web import middleware

from models import init_db


DB_READY_KEY = 'teamsdb:db_ready'


@middleware
async def middleware_init_db(request, handler):
    if DB_READY_KEY not in request.app:
        await init_db(request.app)

        request.app[DB_READY_KEY] = True

    return await handler(request)
