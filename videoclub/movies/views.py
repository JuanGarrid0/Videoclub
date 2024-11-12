from django.http import HttpResponse
from django.shortcuts import render

from .models import Director, Movie

# Create your views here.

movies=["El señor de lls anillos",
        "Juego de Tronos",
        "Pulgarcito",
        "Harry Potter",
        "Karate Kid" ]
directores=[]

generos=["generos"]

list=["lista de movies"]

def index(request):
    return render(request, "movies/index.html", { "items" : movies})

def director(request):
    di=Director.objects.all()
    for item in di:
        directores.append(item.nombre +" "+item.apellido)
    return render(request, "movies/director.html", {"director": directores} )

def genero(request):
    return render(request, "movies/genero.html", {"genero": generos})

def lista(request):
    return render(request, "movies/lista.html",{"lista": list})