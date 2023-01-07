from django import forms


class blogForm(forms.Form):
    titulo=forms.CharField(label="titulo",max_length=50)
    subtitulo=forms.CharField(label="subtitulo",max_length=256,required=False)
    cuerpo=forms.CharField(label="cuerpo",max_length=1024,required=False)
    autor=forms.CharField(label="autor",max_length=50,required=False)
    fecha =forms.DateField (label="fecha",required=False)
    ##imagen =forms.ImageField(label="imagen",)
    pagina_id = forms.IntegerField ()


class pagesForm(forms.Form):
    #id=forms.IntegerField(label="id")
    tema=forms.CharField(label="tema",max_length=50)
    descripcion=forms.CharField(label="descripcion",max_length=256)


##########
class doctorForm(forms.Form):
    nombre= forms.CharField(label="Nombre Doctor", max_length=50)
    apellido= forms.CharField(label="Apellido Doctor", max_length=50)
    email= forms.EmailField(label="Email Doctor")

class veterinariaForm(forms.Form):
    nombre= forms.CharField(label="Nombre veterinaria", max_length=50) 
    direccion= forms.CharField(label="dirección de veterinaria", max_length=50) 

class animalForm(forms.Form):
    nombre = forms.CharField(label="Nombre animal", max_length=50) 
    especie=forms.CharField(label="especie animal", max_length=50)
