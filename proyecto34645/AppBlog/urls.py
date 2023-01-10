from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView




urlpatterns = [
    path("", inicio, name="inicio"),
    path("contacto/", contacto, name="contacto"),
    path("pages/", paginas, name="pages"),
    path("acercade/", acercade, name="acercade"),
    path("blogs/", posteos, name="blogs"),
    path("editarPage/<id>", editarPagina, name="editarPage"),
    path("deletePage/<id>", eliminarPagina, name="deletePage"),
    #login
    path('login/', login_request, name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(template_name='AppBlog/logout.html'), name='logout'),
    path('editarPerfil/', editarPerfil, name='editarPerfil'),
    path('agregarAvatar/', agregarAvatar, name='agregarAvatar'),
]