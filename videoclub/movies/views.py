from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.db.models import Q
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .models import Director, Movie, User

# Create your views here.
#Prueba
def index(request):
    return render(request, "movies/index.html", { "items" : listaMainPage()})

def director(request):
    
    return render(request, "movies/director.html", {"director": getDirectores()} )

def genero(request):
    return render(request, "movies/genero.html", {"genero": getGeneros()})

def lista(request):
    return render(request, "movies/lista.html",{"lista": getLista()})



def login_view(request):
    if request.method == "POST":

        name = request.POST.get("username")
        print(name)
        pas = request.POST.get("password")
        print(pas)
        user = authenticate(request, username=name, password=pas)
        print(user)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "movies/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "movies/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")

        password = request.POST.get("password")
        confirmation = request.POST.get("confirmation")
        if password != confirmation:
            return render(request, "movies/register.html", {
                "message": "Passwords must match."
            })

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "movies/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "movies/register.html")
    

def detalles(request, nombre, tipo):  #detalles pelicula, genero y director
    #return HttpResponse(f"Hola{nombre}")
    if(tipo=="director"):#lista de peliculas 
        name=nombre.split(" ")
        d=Director.objects.get(nombre=name[0], apellido=name[1])
        peli=Movie.objects.values('nombre').filter(directores=d)
        pelis=[]
        for item in peli:
         pelis.append(item.get('nombre'))
        return render(request, "movies/detalles.html", { "tipo":  tipo , "pelis": pelis, "nombre":nombre     })
    
    elif(tipo=="genero"):#lista de peliculas
        peli=Movie.objects.values('nombre').filter(genero=nombre)#devulve queryset de pelis nombre
        a=[]
        for item in peli: #pelis de una en una
            unidadPeli=Movie.objects.get(nombre=item['nombre'])#movie object
            print(unidadPeli)
            dirPelis=""
            counter=0
            for d in unidadPeli.directores.all():
                if(unidadPeli.directores.all().count()-1 > counter):
                    dirPelis= dirPelis +d.nombre+" "+d.apellido+", "
                    counter= counter+1
                else:
                    dirPelis= dirPelis+ d.nombre+" "+d.apellido
            p=[unidadPeli.nombre, 
           unidadPeli.genero, 
           unidadPeli.tipoMovie,
           dirPelis
            ]
            a.append(p)
        return render(request, "movies/detalles.html", { "tipo":  tipo , "peli":a , "genero":nombre   })

    elif(tipo=="lista"):#atributos de la pelicula
        pelis=Movie.objects.get(nombre=nombre)
        directoresPelis=""
        counter=0
        for d in pelis.directores.all():
            if(pelis.directores.all().count()-1 > counter):
                directoresPelis= directoresPelis +d.nombre+" "+d.apellido+", "
                counter= counter+1
            else:
                directoresPelis= directoresPelis+ d.nombre+" "+d.apellido
        p=[pelis.nombre, 
           pelis.genero, 
           pelis.tipoMovie,
           directoresPelis
        ]
        return render(request, "movies/detalles.html", { "tipo":  tipo , "peli": p , "nombre":nombre     })






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

def listaMainPage():
    main=[]
    genero=[]
    m=Movie.objects.all()
    for item in m:
        if (item.genero not in genero ):
          main.append(item.nombre)
          genero.append(item.genero)
    return main

#Busqueda por nombre de director
def buscarDirector(request):
    query = request.GET.get('q')
    dir=[]
    if query:
        # Busca en directores
        directores = Director.objects.filter(Q(nombre__icontains=query) | Q(apellido__icontains=query))
    else:
        directores = []
    for item in directores:
        dir.append(item.nombre +" "+item.apellido)
    return render(request, 'movies/director.html', {
        'director': dir,
    })