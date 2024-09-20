from .index import extended_path
from .decorators import get, post
from django.http import HttpResponse

def route_decorator(func):
    def route_handler(request, *args, **kwargs):
        try:
            result = func(request, *args, **kwargs)
            return HttpResponse(result)
        except Exception as exp:
            return exp

class Router():
    _routes = []

    def get(self,route, middleware):
        self._routes.append((extended_path(route, middleware, method=get)))
    
    def post(self,route, middleware):
        self._routes.append(extended_path(route, middleware, method=post))