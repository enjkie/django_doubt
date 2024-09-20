from django.urls import include
from .views import greet, post_greet
from .common.index import extended_path
from .common.decorators import post
from .users.routes import UserRouter

urlpatterns = [
    extended_path("post_greet", post_greet, method=post),
    extended_path("users", include(UserRouter))
]