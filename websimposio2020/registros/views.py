from django.shortcuts import render
from .forms import Formularioregistro
from django.contrib import messages

# Create your views here.

def inscripcion(request):
    formulario=Formularioregistro(request.POST or None)
    if formulario.is_valid():
        guardar=formulario.save(commit=False)
        guardar.save()
        messages.success(request,'Gracias por registrarte en breve recibiras un correo con la informacion para realizar el pago')
        return HttpResponseRedirect('Inscripcion')
    return render (request,"registros/inscripcion.html",{'form':formulario})