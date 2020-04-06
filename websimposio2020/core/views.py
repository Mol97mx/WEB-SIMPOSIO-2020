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

def talleres(request):
    return render (request,"core/talleres.html")

def panel(request):
    return render (request,"core/panel.html")

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