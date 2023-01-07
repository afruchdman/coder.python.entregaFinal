from django.shortcuts import render

from .models import *
from django.http import HttpResponse
from AppBlog.forms import *

# Create your views here.
def inicio(request):
    return render (request, "AppBlog/inicio.html")

def acercade(request):
    return render (request, "AppBlog/acercade.html")

def contacto(request):
    return render (request, "AppBlog/contacto.html")

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

def posteos(request):
    if request.method=="POST":
        form= blogForm(request.POST)
        if form.is_valid():
            print(1)
            informacion=form.cleaned_data
            #id=informacion["id"]
            titulo= informacion["titulo"]
            subtitulo= informacion["subtitulo"]
            cuerpo= informacion["cuerpo"]
            autor= informacion["autor"]
            fecha= informacion["fecha"]
            pagina_id=informacion["pagina_id"]
            print(titulo)
            print(subtitulo)
            print(cuerpo)
            print(autor)
            print(fecha)
            print(pagina_id)
            b= blogs(titulo=titulo, subtitulo=subtitulo, cuerpo=cuerpo, autor=autor, fecha=fecha,pagina_id=pagina_id)
            b.save()
            posteos=blogs.objects.filter(pagina_id=pagina_id)
            return render(request, "AppBlog/blogs.html" ,{"form": form,"posteos": posteos})
        else:
            print(2)
            return render(request, "AppBlog/blogs.html" ,{"form": form, "mensaje": "Informacion no valida"}) 
    else:
        print(3)
        form= blogForm()
        print("id"+request.GET['pagina_id']) 
        if request.GET['pagina_id']== "":
            posteos=blogs.objects.all()
            return render(request, "AppBlog/blogs.html", {"form": form,"posteos": posteos})  
        else:
            posteos=blogs.objects.filter(pagina_id=request.GET['pagina_id'])
            return render(request, "AppBlog/blogs.html",  {"form": form,"posteos": posteos,"descripcion":request.GET['descripcion'],"tema":request.GET['tema'] ,"origen":request.GET['pagina_id']})


####################################################


# Create your views here.
def doctores(request):
    if request.method=="POST":
        form= doctorForm(request.POST)
        
        if form.is_valid():
            informacion=form.cleaned_data
            nombre= informacion["nombre"]
            apellido= informacion["apellido"]
            email= informacion["email"]
            doc= doctor(nombre=nombre, apellido=apellido, email=email)
            doc.save()
            return render(request, "AppBlog/inicio.html" ,{"mensaje": "Doctor guardado correctamente"})
        else:
            return render(request, "AppBlog/doctores.html" ,{"form": form, "mensaje": "Informacion no valida"})
        
    else:
        formulario= doctorForm()
        return render (request, "AppBlog/doctores.html", {"form": formulario})

def animales(request):
    if request.method=="POST":
        form= animalForm(request.POST)
        
        if form.is_valid():
            informacion=form.cleaned_data
            nombre= informacion["nombre"]
            especie= informacion["especie"]
            anim= animal(nombre=nombre, especie=especie)
            anim.save()
            return render(request, "AppBlog/inicio.html" ,{"mensaje": "Animal guardado correctamente"})
        else:
            return render(request, "AppBlog/animales.html" ,{"form": form, "mensaje": "Informacion no valida"})
        
    else:
        formulario= animalForm()
        return render (request, "AppBlog/animales.html", {"form": formulario})

def veterinarias(request):
    if request.method=="POST":
        form= veterinariaForm(request.POST)
        
        if form.is_valid():
            informacion=form.cleaned_data
            nombre= informacion["nombre"]
            direccion= informacion["direccion"]
            vet= veterinaria(nombre=nombre, direccion=direccion)
            vet.save()
            return render(request, "AppBlog/inicio.html" ,{"mensaje": "Veterinaria guardado correctamente"})
        else:
            return render(request, "AppBlog/veterinarias.html" ,{"form": form, "mensaje": "Informacion no valida"})
        
    else:
        formulario= veterinariaForm()
        return render (request, "AppBlog/veterinarias.html", {"form": formulario})

def busquedaDoctores(request):
    return render(request, "AppBlog/busquedaDoctores.html")

def buscar(request):    
    doctor= request.GET["doctor"]
    if doctor!="":
        doctor= doctor.objects.filter(nombre__icontains=str(doctor) )
        return render(request, "AppBlog/resultadosBusqueda.html", {"nombre": doctor})
    else:
        return render(request, "AppBlog/busquedaDoctores.html", {"mensaje": "Che Ingresa un doctor para buscar!"})