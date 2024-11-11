from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

movies=["El señor de lls anillos",
        "Juego de Tronos",
        "Pulgarcito",
        "Harry Potter",
        "Karate Kid" ]
directores=["directores"]

generos=["generos"]

list=["lista de movies"]

def index(request):
    return render(request, "movies/index.html", { "items" : movies})

def director(request):
    return render(request, "movies/director.html", {"director": directores} )

def genero(request):
    return render(request, "movies/genero.html", {"genero": generos})

def lista(request):
    return render(request, "movies/lista.html",{"lista": list})