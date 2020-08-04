from django.db import models

# Create your models here.
Opciones_paquetes = [
    ('Simposio', 'Asistencia al simposio $1,595.00 MXN'),
    ('Curso Valuacion de bienes distintos a la tierra', 'Curso Valuación de bienes distintos a la tierra $1,595.00 MXN'),
    ('Curso Valuacion de inmuebles rusticos con presion urbana', 'Curso Valuación de inmuebles rústicos con presión urbana $1,595.00 MXN'),
    ('Curso Valuacion economica de impacto ambiental por el Metodo de valoracion contingente', 'Curso Valuación económica de impacto ambiental por el Método de Valoración Contingente $1,595.00 MXN'),
    ('Simposio y curso Valuacion de bienes distintos a la tierra', 'Simposio y curso Valuación de bienes distintos a la tierra $2,900.00 MXN'),
    ('Simposio y curso Valuacion de inmuebles rusticos con presion urbana', 'Simposio y curso Valuacion de inmuebles rusticos con presion urbana $2,900.00 MXN'),
    ('Simposio y curso Valuacion economica de impacto ambiental por el Metodo de valoracion contingente', 'Simposio y curso Valuación económica de impacto ambiental por el Método de Valoración Contingente $2,900.00 MXN'),
]
OPCIONES=[('pendiente','Pendiente de pago'),('pagado','Pago confirmado')]

class registro(models.Model):
    nombre=models.CharField(max_length=80)
    rfc=models.CharField(max_length=13)
    email=models.EmailField()
    telefono=models.CharField(max_length=20)
    universidad=models.CharField(max_length=50)
    calle=models.CharField(max_length=50)
    numeroexterior=models.CharField(max_length=6)
    numerointerior=models.CharField(max_length=6,blank=True)
    colonia=models.CharField(max_length=50)
    cp=models.CharField(max_length=10)
    ciudad=models.CharField(max_length=50)
    estado=models.CharField(max_length=50)
    pais=models.CharField(max_length=50)
    cfdi=models.CharField(max_length=5,blank=True)
    formadepago=models.CharField(max_length=30,blank=True)
    metododepago=models.CharField(max_length=30,blank=True)
    opcion=models.CharField(max_length=100,verbose_name="Paquete seleccionado",choices=Opciones_paquetes)
    pagado=models.CharField(max_length=50,choices=OPCIONES,default='pendiente')
    fechaderegistro=models.DateTimeField(auto_now_add=True,verbose_name="Fecha de registro")
    fechademodificacion=models.DateTimeField(auto_now=True,verbose_name="Fecha de modificacion")

    class Meta:
        ordering=['fechaderegistro']

    def __str__(self):
        return self.email