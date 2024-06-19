from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length = 100)
    apellidos = models.CharField(max_length = 100)
    edad = models.IntegerField(blank = True)
    donador = models.BooleanField(default= False)
    
    def get_absolute_url(self):
        return "/personas/" + str(self.id) + "/"

# Create your models here.