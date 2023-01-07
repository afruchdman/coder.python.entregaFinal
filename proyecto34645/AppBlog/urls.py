from django.urls import path
from .views import *



urlpatterns = [
    path("", inicio, name="inicio"),
    path("contacto/", contacto, name="contacto"),
    path("pages/", paginas, name="pages"),
    path("acercade/", acercade, name="acercade"),
    path("blogs/", posteos, name="blogs"),
    #path("veterinarias/", veterinarias, name="veterinarias"),
    #path("busquedaDoctores/", busquedaDoctores, name="busquedaDoctores"),
    #path("buscar/", buscar, name="buscar"),

]