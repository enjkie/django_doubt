from django.urls import path 

def extended_path(route, view, kwargs=None, name=None, method=None):
    if(method != None):
        view = method(view)
    return path(route, view, kwargs=kwargs, name=name)