from django.http import HttpResponse

def get_users():
    HttpResponse('[GET] users')

def post_users():
    HttpResponse('[POST] users')

def put_users():
    HttpResponse('[PUT] users')

def delete_users():
    HttpResponse('[PATCH] users')