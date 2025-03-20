from typing import Callable
from fastapi import Request as RequestFastApi

async def request_adapter(request: RequestFastApi, callback: Callable):
    ''' Fast API Adapter '''

    body = None

    try:
        body = await request.json()
    except:
        pass 

    http_request = {
        'query_params': request.query_params,
        'body': body
    }

    http_request = callback(http_request)
    return http_request