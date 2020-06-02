from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Galeria(models.Model):
    titulo=models.CharField(max_length=200)
    descripcion=models.TextField()
    imagen=models.ImageField(upload_to="imagenes")
    creado=models.DateTimeField(auto_now_add=True)
    actualizado=models.DateTimeField(auto_now=True)
    autor= models.ForeignKey(User,on_delete=models.PROTECT,null=True,blank=True)

    class Meta:
        verbose_name="Imagen"
        verbose_name_plural="Imagenes"
        ordering=["-creado"]

    def __str__(self):
        return self.titulo