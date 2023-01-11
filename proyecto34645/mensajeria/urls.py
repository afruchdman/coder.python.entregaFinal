from django.urls import path
from .views import *



urlpatterns = [
    path("", enviar, name="enviar"),
    path("mensajes/", leer, name="mensajes"),
    path("leer/", leer, name="leer"),
]