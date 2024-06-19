from django.shortcuts import render, get_object_or_404
from .models import Persona
from .forms import RawPersonaForm, PersonaForm

# Create your views here.
def personasAnotherCreateView(request):
    form = RawPersonaForm()
    if request.method == "POST":
        form = RawPersonaForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            
        else:
            print(form.errors)
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
    
def personasShowObjects(request, myID):
    obj = get_object_or_404(Persona, id = myID)
    context = {
        'objeto': obj
        }
    return render(request, 'personas/descripcion.html', context)