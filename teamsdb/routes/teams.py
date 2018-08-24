from operator import itemgetter

from aiohttp import web

from models import Person

from routes import routes


@routes.get('/api/v1/teams/{id}/members')
async def teams_member(request):
    team = await Person.get(int(request.match_info['id']))

    if not team:
        return web.Response(status=404)

    if not team.is_team:
        return web.json_response({
            'error': 'Requested to get members of a non-team',
        }, status=400)

    members = await team.get_members()

    return web.json_response(list(map(itemgetter(1), members)))
