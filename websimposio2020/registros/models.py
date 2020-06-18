from django.db import models

# Create your models here.
Opciones_paquetes = [
    ('Curso Valuacion de bienes distintos a la tierra', 'Curso Valuación de bienes distintos a la tierra $1,375.00 MXN'),
    ('Curso Valuacion de inmuebles rusticos con presion urbana', 'Curso Valuación de inmuebles rústicos con presión urbana $1,375.00 MXN'),
    ('Curso Valuacion economica de impacto ambiental por el Metodo de valoracion contingente', 'Curso Valuación económica de impacto ambiental por el Método de Valoración Contingente $1,375.00 MXN'),
    ('Simposio y curso', 'Simposio y curso $2,500.00 MXN'),
]

class registro(models.Model):
    nombre=models.CharField(max_length=20)
    apellidop=models.CharField(max_length=20)
    apellidom=models.CharField(max_length=20)
    email=models.EmailField()
    telefono=models.CharField(max_length=20)
    universidad=models.CharField(max_length=50)
    opcion=models.CharField(max_length=100,verbose_name="Paquete seleccionado",choices=Opciones_paquetes)
    fechaderegistro=models.DateTimeField(auto_now_add=True,verbose_name="Fecha de registro")
    fechademodificacion=models.DateTimeField(auto_now=True,verbose_name="Fecha de modificacion")

    class Meta:
        ordering=['fechaderegistro']

    def __str__(self):
        return self.email