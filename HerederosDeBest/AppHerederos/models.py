from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Integrantes(models.Model):
    nombre=models.CharField(max_length=25)
    apellido=models.CharField(max_length=25)
    apodo=models.CharField(max_length=25)
    fechaDeNacimiento=models.DateField()

class ProximasFechas(models.Model):
    nombreDeLaFiesta=models.CharField(max_length=50)
    lugar=models.CharField(max_length=255)
    fechaDeLaFiesta=models.DateField()

class Anecdotas(models.Model):
    titulo=models.CharField(max_length=40)
    relato=models.TextField()

class Lugares(models.Model):
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=255)
    