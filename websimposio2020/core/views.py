from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from django.http import JsonResponse
import stripe
stripe.api_key = "sk_test_vkm9UX8dSGs3JNkDWf0OiBf700Hqs16iz4"
# Create your views here.

def home(request):
    return render (request,"core/home.html")

def informacion(request):
    return render (request,"core/informacion.html")
    
def resumenes(request):
    return render (request,"core/resumenes.html")

def instructores(request):
    return render (request,"core/instructores.html")

def calendario(request):
    return render (request,"core/calendario.html")

def semblanzaGPA(request):
    return render (request,"core/semblanzaGPA.html")

def semblanzaCCM(request):
    return render (request,"core/semblanzaCCM.html")

def semblanzaVMHM(request):
    return render (request,"core/semblanzaVMHM.html")

def semblanzaOPV(request):
    return render (request,"core/semblanzaOPV.html")

def semblanzaNFL(request):
    return render (request,"core/semblanzaNFL.html")

def semblanzaMLL(request):
    return render (request,"core/semblanzaMLL.html")

def semblanzaPBL(request):
    return render (request,"core/semblanzaPBL.html")

def patrocinadores(request):
    return render (request,"core/patrocinadores.html")

def contacto(request):
    return render (request,"core/contacto.html")

def acerca(request):
    return render (request,"core/acerca.html")

def quienes(request):
    return render (request,"core/quienes.html")

def precios(request):
    return render (request,"core/precios.html")

def talleres(request):
    return render (request,"core/talleres.html")

def conferencias(request):
    return render (request,"core/conferencias.html")

def conferencistas(request):
    return render (request,"core/conferencistas.html")

def ponencias(request):
    return render (request,"core/ponencias.html")

def simposio(request):
    return render (request,"core/simposio.html")