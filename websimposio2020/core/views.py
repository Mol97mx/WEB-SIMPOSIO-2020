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

def charge(request):
    if request.method=='POST':
        print('Data:', request.POST)
        amount=int(request.POST['amount'])
        cliente=stripe.Customer.create(
            email=request.POST['email'],
            name=request.POST['name'],
            description=request.POST['instituto'],
            source=request.POST['stripeToken']
        )
        cargo=stripe.Charge.create(
            customer=cliente,
            amount=amount*100,
            currency="mxn",
            description="Pago por sólo asistencia"
        )
    return redirect(reverse ('success', args=[amount]))

def success(request, args):
    amount=args
    return render(request,"core/success.html",{'amount':amount})