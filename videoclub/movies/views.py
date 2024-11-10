from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

movies=["El señor de lls anillos",
        "Juego de Tronos",
        "Pulgarcito",
        "Harry Potter",
        "Karate Kid" ]

def index(request):
    return render(request, "movies/index.html", { "items" : movies})

def director():
    return

def genero():
    return

def lista():
    return