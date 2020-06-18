from django import forms
from .models import registro

class Formularioregistro(forms.ModelForm):
    class Meta:
        model=registro
        fields=['nombre','apellidop','apellidom','email','telefono','universidad','opcion']