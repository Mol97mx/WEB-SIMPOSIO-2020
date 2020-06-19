from django.shortcuts import render,HttpResponseRedirect
from django.conf import settings
from django.core.mail import send_mail
from .forms import Formularioregistro
from django.contrib import messages

# Create your views here.

def inscripcion(request):
    formulario=Formularioregistro(request.POST or None)
    if formulario.is_valid():
        guardar=formulario.save(commit=False)
        guardar.save()
        subject="Confirmacion de incripcion al simposio"
        message="Agradecemos tu incripcion y quedamos a la espera del deposito o transferencia para confirmar tu lugar, deberas hacer al deposito o transferencia a la siguiente cuenta: INSTITUTO NACIONAL DE VALUACIÓN AGROPECUARIA Y FORESTAL DE MICHOACÁN, AC BANCO: BANBAJÍO CUENTA: 1293 3826 0201 CLABE: 0305 3590 0004 4494 80"
        from_email=settings.EMAIL_HOST_USER
        to_list=[guardar.email,settings.EMAIL_HOST_USER]
        send_mail(subject,message,from_email,to_list,fail_silently=True)
        messages.success(request,'Gracias por registrarte en breve recibiras un correo con la informacion para realizar el pago')
        return HttpResponseRedirect('/gracias')
    return render (request,"registros/inscripcion.html",{'form':formulario})
