from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

def myHomeview(request, *args, **kwargs):
    myContext = {
        'myText': 'Esto es sobre mi',
        'myNumber': 123,
        'myList': [22,33,44,55,66],
    }
    return render(request, 'home.html', myContext)
  
def anotherView(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return HttpResponse('<h1>Otra vista desde DJango</h1>')