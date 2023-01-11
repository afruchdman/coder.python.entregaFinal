from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from mensajeria.forms import *
from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate

# Create your views here.



def leer(request):
    print(request.user)
    m= msg.objects.filter(receptor=request.user )
    print(len(m))
    return render(request, "mensajeria/mensajes.html", {"mensajes": m})

def enviar(request):
    print(request.method)
    if request.method=="POST":
        form= msgForm(request.POST)
        
        if form.is_valid():
            informacion=form.cleaned_data
            mensage= informacion["msg"]
            emisor= request.user #  informacion["emisor"]
            if request.user == None or request.user == "":
                emisor =informacion["emisor"]
            receptor= informacion["receptor"]
            leido= informacion["leido"]
            print(request.user)
            m= msg(msg=mensage, emisor=emisor, receptor=receptor,leido=bool(leido))
            m.save()
            return render(request, "mensajeria/enviar.html" ,{"mensaje": "mensaje enviado a " +  receptor  ,"form": form})
        else:
            return render(request, "mensajeria/enviar.html" ,{"form": form, "mensaje": "mensaje mal formado"})
        
    else:
        form= msgForm()
        return render (request, "mensajeria/enviar.html", {"form": form,"mensaje": ""})
