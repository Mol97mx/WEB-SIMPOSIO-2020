from django import forms
from .models import registro

class Formularioregistro(forms.ModelForm):
    nombre = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class':'form-control main', 'placeholder':'Nombre completo o Razón social...'}
    ))
    rfc = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class':'form-control main', 'placeholder':'RFC...'}
    ))
    calle = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class':'form-control main', 'placeholder':'Calle...'}
    ))
    numeroexterior = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class':'form-control main', 'placeholder':'Numero...'}
    ))
    numerointerior = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class':'form-control main', 'placeholder':'Numero interior...'}
    ))
    colonia = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class':'form-control main', 'placeholder':'Colonia...'}
    ))
    ciudad = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class':'form-control main', 'placeholder':'Municipio...'}
    ))
    estado= forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class':'form-control main', 'placeholder':'Estado...'}
    ))
    pais = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class':'form-control main', 'placeholder':'País...'}
    ))
    telefono = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class':'form-control main', 'placeholder':'Telefono...'}
    ))
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'class':'form-control main', 'placeholder':'Email...'}
    ))
    cfdi = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class':'form-control main', 'placeholder':'Uso del CFDI...'}
    ))
    formadepago = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class':'form-control main', 'placeholder':'Forma de pago...'}
    ))
    metododepago = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class':'form-control main', 'placeholder':'Metodo de pago...'}
    ))
    universidad = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class':'form-control main', 'placeholder':'¿De qué universidad nos visitas?'}
    ))
    class Meta:
        model=registro
        fields=['nombre','rfc','calle','numeroexterior','numerointerior','colonia','ciudad','estado','pais','email','telefono','cfdi','formadepago','metododepago','universidad','opcion']