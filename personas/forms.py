from django import forms
from .models import Persona

class RawPersonaForm(forms.Form):
    nombre = forms.CharField()
    apellidos = forms.CharField()
    edad = forms.IntegerField()
    donador = forms.BooleanField()