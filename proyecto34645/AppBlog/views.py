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





def leerPaginas(request):
    p=pages.objects.all()
    return render(request, "AppBlog/editarPage.html", {"pages": p})

def eliminarPagina(request, id):
    p=pages.objects.get(id=id)
    p.delete()
    p=pages.objects.all()
    return render(request, "AppBlog/pages.html", {"paginas": p, "mensaje": "Pagina eliminado correctamente"})

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

 