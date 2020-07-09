from django import forms
from .models import registro

class Formularioregistro(forms.ModelForm):
    nombre = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class':'form-control main', 'placeholder':'Nombre...'}
    ))
    apellidop = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class':'form-control main', 'placeholder':'Apellido paterno...'}
    ))
    apellidom = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class':'form-control main', 'placeholder':'Apellido materno...'}
    ))
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'class':'form-control main', 'placeholder':'Email...'}
    ))
    telefono = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class':'form-control main', 'placeholder':'Telefono...'}
    ))
    estado= forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class':'form-control main', 'placeholder':'Estado...'}
    ))
    ciudad = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class':'form-control main', 'placeholder':'Ciudad...'}
    ))
    universidad = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class':'form-control main', 'placeholder':'¿De qué universidad nos visitas?'}
    ))
    class Meta:
        model=registro
        fields=['nombre','apellidop','apellidom','email','telefono','ciudad','estado','universidad','opcion']