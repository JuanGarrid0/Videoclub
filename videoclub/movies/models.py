from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Director(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)

class Movie (models.Model):
    movies= (("Pelicula", "Pelicula"), ("Serie", "Serie"))
    genero = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    directores = models.ManyToManyField(Director, null=True, blank=True)
    tipoMovie = models.CharField(choices=movies, max_length=20)

class User(AbstractUser):
    pass