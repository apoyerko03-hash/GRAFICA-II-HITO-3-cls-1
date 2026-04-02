from django.urls import path
from .views import obtener_posts, crear_post
urlpatterns = [
    path('posts/', obtener_posts),
    path('crear/', crear_post),
]