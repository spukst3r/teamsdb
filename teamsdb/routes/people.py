from operator import attrgetter

from aiohttp import web

from models import Person

from routes import routes


@routes.get('/api/v1/people/{id}/teams')
async def people_teams(request):
    person = await Person.get(int(request.match_info['id']))

    if person is None:
        return web.Response(status=404)

    teams = await person.get_teams(order_by='name')

    return web.json_response(list(map(attrgetter('name'), teams)))
