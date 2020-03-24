from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render (request,"core/home.html")

def informacion(request):
    return render (request,"core/informacion.html")

def inscripcion(request):
    return render (request,"core/inscripcion.html")
    
def resumenes(request):
    return render (request,"core/resumenes.html")