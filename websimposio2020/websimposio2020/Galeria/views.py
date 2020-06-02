from django.shortcuts import render
from .models import Galeria

# Create your views here.

def galeria(request):
    imagenes=Galeria.objects.all()
    return render(request,"Galeria/galeria.html",{'Galeria':imagenes})