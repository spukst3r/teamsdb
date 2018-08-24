import os
import pkgutil

from aiohttp import web


def load_routes(module):
    dirname = os.path.dirname(pkgutil.get_loader(module).get_filename())

    for path, directories, files in os.walk(dirname):
        for importer, package_name, ispkg in pkgutil.iter_modules([path]):
            importer.find_module(package_name).load_module(package_name)


routes = web.RouteTableDef()


load_routes('routes')
