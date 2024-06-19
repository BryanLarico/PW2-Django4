from django.shortcuts import render
from .models import Persona
from .forms import RawPersonaForm

# Create your views here.
def personasAnotherCreateView(request):
    form = RawPersonaForm()
    context = {
        'form': form,
        }
    return render(request, 'personas/personasCreate.html', context)

def personaTestView(request, *args, **kwargs):
    obj = Persona.objects.get(id = 1)
    context = {
        'objeto': obj,
        }
    return render(request, 'personas/descripcion.html', context)

def personaCreateView(request, *args, **kwargs):
    print(request)
    if request.method == 'POST':
        nombre = request.POST.get('q')
        print(nombre)
    context = {}
    return render(request, 'personas/personasCreate.html', context)
    
def searchForHelp(request):
    return render(request, 'personas/search.html', {})