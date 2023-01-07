from django.urls import path
from .views import *



urlpatterns = [
    path("", inicio, name="inicio"),
    path("contacto/", contacto, name="contacto"),
    path("pages/", paginas, name="pages"),
    path("acercade/", acercade, name="acercade"),
    path("blogs/", posteos, name="blogs"),
    path("editarPage/<id>", editarPagina, name="editarPage"),
    path("deletePage/<id>", eliminarPagina, name="deletePage"),
]