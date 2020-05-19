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

def charge(request):
    if request.method=='POST':
        print('Data:', request.POST)
        if request.POST['amount']=='evento':
            amount=int(1375)
            desc="Inscripción al simposio"
        elif request.POST['amount']=='curso':
            amount=int(1375)
            desc="Inscripción a curso"
        else:
            amount=int(2500)
            desc="Inscripción a cursos y simposio"
        try:
        # Use Stripe's library to make requests...
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
                description=desc,
            )
            return redirect(reverse ('success', args=[amount]))
            pass
        except stripe.error.CardError as e:
            # Since it's a decline, stripe.error.CardError will be caught
            #print('Status is: %s' % e.http_status)
            #print('Type is: %s' % e.error.type)
            #print('Code is: %s' % e.error.code)
            # param is '' in this case
            #print('Param is: %s' % e.error.param)
            #print('Message is: %s' % e.error.message)
            return redirect(reverse ('failure', args=[e.error.message]))
        except stripe.error.RateLimitError as e:
            # Too many requests made to the API too quickly
            return redirect(reverse ('failure', args=[e.error.message]))
            pass
        except stripe.error.InvalidRequestError as e:
            # Invalid parameters were supplied to Stripe's API
            return redirect(reverse ('failure', args=[e.error.message]))
            pass
        except stripe.error.AuthenticationError as e:
            # Authentication with Stripe's API failed
            # (maybe you changed API keys recently)
            return redirect(reverse ('failure', args=[e.error.message]))
            pass
        except stripe.error.APIConnectionError as e:
            # Network communication with Stripe failed
            return redirect(reverse ('failure', args=[e.error.message]))
            pass
        except stripe.error.StripeError as e:
            # Display a very generic error to the user, and maybe send
            # yourself an email
            return redirect(reverse ('failure', args=[e.error.message]))
            pass
        except Exception as e:
            # Something else happened, completely unrelated to Stripe
            return redirect(reverse ('failure', args=[e.error.message]))
            pass

def success(request, args):
    amount=args
    return render(request,"core/success.html",{'amount':amount})

def failure(request, args):
    mensaje=args
    return render(request,"core/failure.html",{'mensaje':mensaje})