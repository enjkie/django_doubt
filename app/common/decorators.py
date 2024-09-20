from django.http import HttpRequest, HttpResponse

class methods:
    POST   = 'POST'
    GET    = 'GET'
    PUT    = 'PUT'
    PATCH  = 'PATCH'
    DELETE = 'DELETE' 

def method_deco(method:methods):
    def deco(func):
        def handler(request: HttpRequest, *args, **kwargs):
            if(request.method != method):
                return HttpResponse(f"Cannot {request.method} '{request.path}'")

            return func(request, *args, **kwargs)

        return handler
    return deco

post   = method_deco('POST')
get    = method_deco('GET')
put    = method_deco('PUT')
patch  = method_deco('PATCH')
delete = method_deco('DELETE')