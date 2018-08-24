import asyncio
import os

from aiohttp import web

from config import load_config

from middleware.error_handler import middleware_error_handler
from middleware.init_db import middleware_init_db

from routes import routes


app = web.Application(
    middlewares=[
        middleware_error_handler,
        middleware_init_db,
    ],
)

app.add_routes(routes)
app['config'] = load_config(os.environ.get('CONFIG'))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    web.run_app(app, port=app['config']['app']['port'])
