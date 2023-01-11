from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#from _ckeditor.fields import RichTextFormField
#from _ckeditor.widgets import CKEditorWidget



class blogForm(forms.Form):
    titulo=forms.CharField(label="titulo",max_length=50)
    subtitulo=forms.CharField(label="subtitulo",max_length=256,required=False)
    cuerpo=forms.CharField(widget=forms.Textarea(attrs={
        'rows' : 4,
        'class' : 'answers',
        }))
    autor=forms.CharField(label="autor",max_length=50,required=False)
    fecha =forms.DateField (label="fecha",required=False)
    imagen =forms.ImageField(  label="imagen",required=False)
    pagina_id = forms.IntegerField ()


class pagesForm(forms.Form):
    #id=forms.IntegerField(label="id")
    tema=forms.CharField(label="tema",max_length=50)
    descripcion=forms.CharField(label="descripcion",max_length=256)

############ registro #####################
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)
    first_name= forms.CharField(max_length=50)
    last_name= forms.CharField(max_length=50)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)
    first_name= forms.CharField(max_length=50)
    last_name= forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']
        help_texts = {k:"" for k in fields}
    

class AvatarForm(forms.Form):
    imagen= forms.ImageField(label="Imagen")