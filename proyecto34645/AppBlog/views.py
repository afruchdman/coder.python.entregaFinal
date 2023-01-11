from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.urls import reverse_lazy
from AppBlog.forms import *
from AppBlog.forms import UserRegisterForm, UserEditForm, AvatarForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
def inicio(request):
    return render (request, "AppBlog/inicio.html")

@login_required
def acercade(request):
    return render (request, "AppBlog/acercade.html")

@login_required
def contacto(request):
    return render (request, "AppBlog/contacto.html")

@login_required
def paginas(request):
    if request.method=="POST":
        form= pagesForm(request.POST)
        
        if form.is_valid():
            informacion=form.cleaned_data
            #id=informacion["id"]
            tema= informacion["tema"]
            descripcion= informacion["descripcion"]
            p= pages(tema=tema, descripcion=descripcion)
            p.save()
            paginas=pages.objects.all()
            return render(request, "AppBlog/pages.html" ,{"form": form,"paginas": paginas})
        else:
            return render(request, "AppBlog/pages.html" ,{"form": form, "mensaje": "Informacion no valida"}) 
    else:
        form= pagesForm()
        paginas=pages.objects.all()
        return render(request, "AppBlog/pages.html", {"form": form,"paginas": paginas})

@login_required
def posteos(request):
    if request.method=="POST":
        form= blogForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            #id=informacion["id"]
            titulo= informacion["titulo"]
            subtitulo= informacion["subtitulo"]
            cuerpo= informacion["cuerpo"]
            autor= informacion["autor"]
            fecha= informacion["fecha"]
            imagen= informacion["imagen"]
            if informacion["imagen"] == None:
                imagen="/static/assets/img/default.jpg"
            pagina_id=informacion["pagina_id"]
            b= blogs( imagen=imagen,titulo=titulo, subtitulo=subtitulo, cuerpo=cuerpo, autor=autor, fecha=fecha, pagina_id=pagina_id)
            b.save()
            posteos=blogs.objects.filter(pagina_id=pagina_id)
            return render(request, "AppBlog/blogs.html" ,{"form": form,"posteos": posteos})
        else:
            return render(request, "AppBlog/blogs.html" ,{"form": form, "mensaje": "Informacion no valida"}) 
    else:
        form= blogForm()
        print("id"+request.GET['pagina_id']) 
        if request.GET['pagina_id']== "":
            posteos=blogs.objects.all()
            return render(request, "AppBlog/blogs.html", {"form": form,"posteos": posteos})  
        else:
            posteos=blogs.objects.filter(pagina_id=request.GET['pagina_id'])
            return render(request, "AppBlog/blogs.html",  {"form": form,"posteos": posteos,"descripcion":request.GET['descripcion'],"tema":request.GET['tema'] ,"origen":request.GET['pagina_id']})





@login_required
def leerPaginas(request):
    p=pages.objects.all()
    return render(request, "AppBlog/editarPage.html", {"pages": p})

@login_required
def eliminarPagina(request, id):
    p=pages.objects.get(id=id)
    p.delete()
    p=pages.objects.all()
    return render(request, "AppBlog/pages.html", {"paginas": p, "mensaje": "Pagina eliminado correctamente"})

@login_required
def editarPagina(request, id):
    p=pages.objects.get(id=id)
    if request.method=="POST":
        form= pagesForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            #id=informacion["id"]
            p.tema= informacion["tema"]
            p.descripcion= informacion["descripcion"]
            p.save()
            return render(request, "AppBlog/editarPage.html" ,{"pagina":p, "mensaje": "Pagina editado correctamente"})
        pass
    else:
        form= pagesForm(initial={"tema":p.tema, "descripcion":p.descripcion})
        return render(request, "AppBlog/editarPage.html", {"form": form, "pagina": p})

#-----------------
def login_request(request):
    if request.method=="POST":
        form = AuthenticationForm(request, data=request.POST )
        if form.is_valid:
            usu= request.POST['username']
            clave= request.POST['password']
            
            usuario = authenticate(username=usu, password=clave)
            
            if usuario is not None:
                login(request, usuario)
                return render(request, 'AppBlog/inicio.html', {'form':form,'mensaje':f"Bienvenido {usuario}"})
            else:
                return render(request, 'AppBlog/login.html', {'form':form,'mensaje':f"Usuario o clave incorrectos"})
        else:
            return render(request, 'AppBlog/login.html', {'form':form,'mensaje':f"FORMULARIO INVALIDO"})
    else:
        form = AuthenticationForm()
        return render(request, 'AppBlog/login.html', {'form':form})


@login_required
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]

            form.save()
            return render(request, 'AppBlog/inicio.html', {'form':form,'mensaje':f"Usuario Creado:  {username}"})
    else:
        form = UserRegisterForm()
    return render(request, 'AppBlog/register.html', {'form': form})

            


@login_required
def editarPerfil(request):
    usuario=request.user

    if request.method == 'POST':
        formulario=UserEditForm(request.POST, instance=usuario)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            usuario.email=informacion['email']
            usuario.password1=informacion['password1']
            usuario.password2=informacion['password2']
            usuario.save()
            return render(request, 'AppBlog/inicio.html', {'usuario':usuario, 'mensaje':'PERFIL EDITADO EXITOSAMENTE'})
    else:
        formulario=UserEditForm(instance=usuario)
    return render(request, 'AppBlog/editarPerfil.html', {'formulario':formulario, 'usuario':usuario.username})
    
