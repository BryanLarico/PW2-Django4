from django import forms
from .models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = [
            'nombre',
            'apellidos',
            'edad',
            'donador',
            ]
    def clean_nombre(self, *args, **kwargs):
        print('paso')
        name = self.cleaned_data.get('nombre')
        if name.istitle():
            return name;
        else:
            raise forms.ValidationError('Primera letra en Mayúscula')