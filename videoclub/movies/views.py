from django.http import HttpResponse
from django.shortcuts import render

from .models import Director, Movie

# Create your views here.

def index(request):
    return render(request, "movies/index.html", { "items" : listaMainPage()})

def director(request):
    
    return render(request, "movies/director.html", {"director": getDirectores()} )

def genero(request):
    return render(request, "movies/genero.html", {"genero": getGeneros()})

def lista(request):
    return render(request, "movies/lista.html",{"lista": getLista()})


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
                    dirPelis= d.nombre+" "+d.apellido+" ,"
                    counter= counter+1
                else:
                    dirPelis= d.nombre+" "+d.apellido+" "
            p=[unidadPeli.nombre, 
           unidadPeli.genero, 
           unidadPeli.tipoMovie,
           dirPelis
            ]
            a.append(p)
        return render(request, "movies/detalles.html", { "tipo":  tipo , "peli":a      })

    elif(tipo=="lista"):#atributos de la pelicula
        pelis=Movie.objects.get(nombre=nombre)
        directoresPelis=""
        counter=0
        for d in pelis.directores.all():
            if(pelis.directores.all().count()-1 > counter):
                directoresPelis= d.nombre+" "+d.apellido+" ,"
                counter= counter+1
            else:
                directoresPelis= d.nombre+" "+d.apellido+" "
        p=[pelis.nombre, 
           pelis.genero, 
           pelis.tipoMovie,
           directoresPelis
        ]
        return render(request, "movies/detalles.html", { "tipo":  tipo , "peli": p      })






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

