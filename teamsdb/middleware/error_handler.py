from aiohttp.web import json_response, middleware


@middleware
async def middleware_error_handler(request, handler):
    try:
        return await handler(request)
    except Exception:
        # Return a generic pretty json.
        # Maybe send the error report.

        return json_response({
            'error': 'Sorry, something went wrong',
        }, status=500)
