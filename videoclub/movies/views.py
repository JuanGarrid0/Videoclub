from django.http import HttpResponse
from django.shortcuts import render

from .models import Director, Movie

# Create your views here.

movies=["El señor de lls anillos",
        "Juego de Tronos",
        "Pulgarcito",
        "Harry Potter",
        "Karate Kid" ]



def index(request):
    return render(request, "movies/index.html", { "items" : movies})

def director(request):
    
    return render(request, "movies/director.html", {"director": getDirectores()} )

def genero(request):
    return render(request, "movies/genero.html", {"genero": getGeneros()})

def lista(request):
    return render(request, "movies/lista.html",{"lista": getLista()})


def getDirectores():
    directores=[]
    di=Director.objects.all()
    for item in di:
        directores.append(item.nombre +" "+item.apellido)
    return directores

def getGeneros():
    generos=[]
    g=Movie.objects.all()
    for item in g:
        if (item.genero not in generos):
         generos.append(item.genero)
    return generos

def getLista():
    lista=[]
    l=Movie.objects.all()
    for item in l:
        lista.append(item.nombre)
    return lista  
