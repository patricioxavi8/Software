from django.db import models

from django.contrib.auth.models import AbstractUser


class Persona(AbstractUser):
    id_persona = models.CharField(max_length=10,primary_key=True,unique=True)
    pais = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    sexo = models.CharField(max_length=1)
    #fecha_nacimiento = models.DateField(blank=True)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_supervisor = models.BooleanField(default=False)

    
    def __str__(self):
        return self.first_name + " " + self.last_name