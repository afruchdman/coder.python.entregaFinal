from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class pages(models.Model):
    #id=models.IntegerField(primary_key=True)
    tema=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=256,null=True)
    def __str__(self):
        return f"{self.tema} - {str(self.descripcion)}"

class blogs(models.Model):
    titulo=models.CharField(max_length=50,null=True)
    subtitulo=models.CharField(max_length=256,null=True)
    cuerpo=models.CharField(max_length=1024,null=True)
    autor=models.CharField(max_length=50,null=True)
    fecha =models.DateField(null=True)
    imagen =models.ImageField(null=True)
    pagina_id = models.IntegerField(null=True)
    #pagina_id = models.ForeignKey(pages, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return f"{self.titulo} - {str(self.subtitulo)}"


class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    imagen= models.ImageField(upload_to='avatares', null=True, blank=True)