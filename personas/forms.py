from django import forms
from .models import Persona

class RawPersonaForm(forms.Form):
    nombre = forms.CharField(label = 'Your name')
    apellidos = forms.CharField()
    edad = forms.IntegerField(initial = 20)
    donador = forms.BooleanField()