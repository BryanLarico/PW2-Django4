from django.db import models
from django.urls import reverse

class Persona(models.Model):
    nombre = models.CharField(max_length = 100)
    apellidos = models.CharField(max_length = 100)
    edad = models.IntegerField(blank = True)
    donador = models.BooleanField(default= False)
    
    def get_absolute_url(self):
        return reverse('personas:browsing', kwargs={'myID': self.id})

# Create your models here.