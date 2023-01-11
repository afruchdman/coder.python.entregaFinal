from django.db import models

class msg(models.Model):
    msg=models.CharField(max_length=1024,null=True)
    emisor=models.CharField(max_length=256,null=False)
    receptor=models.CharField(max_length=256,null=True)
    leido=models.BooleanField(default=False)
    def __str__(self):
        return f"{self.emisor} - {str(self.receptor)}"