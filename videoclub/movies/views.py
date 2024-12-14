from django.db import IntegrityError

from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.db.models import Q
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .models import Director, Movie, Reserva, User

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

def formulario(request):
    return render(request, "movies/formulario.html")


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
            return render(request, "movies/index.html", {"user_logged_in": True})
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

#Busuqeda por nombre de película (Para JavaScript)
def buscarPeliculas(request):
    lista = getLista()
    query = request.GET.get('q', '')
    if query:
        resultados = [entry for entry in lista if query.lower() in entry.lower()]
    else:
        resultados = lista
    
    return JsonResponse({'results': resultados})

def delete(request, peli):
    if request.method == "POST":
        movie= Movie.objects.get(nombre=peli)
        movie.delete()
        return HttpResponseRedirect(reverse("index"))
    
def nombreToId(peli):
    movie= Movie.objects.get(nombre=peli)
    id = movie.id
    return id 

def updatePage(request,peli ):
    if request.method == "POST":
            try:
                movie = Movie.objects.get(nombre=peli)
                id=movie.id

            except Movie.DoesNotExist:
                raise Http404("Movie not found") 
                       
            try:
                movie= Movie.objects.get(id=id)
                directores=movie.directores.values()
                return render(request,'movies/update.html',{"movie":movie,"directores":directores  })

            except Movie.DoesNotExist:
                raise Http404("Movie not found") 
           
 


def update(request, peli):
    movie= Movie.objects.get(id=peli)
    if request.method =="POST":
        nombre = request.POST.get("nombre")
        if nombre is not None:
            movie.nombre=nombre
            movie.save()


        genero = request.POST.get("genero")
        if genero is not None:
            movie.genero=genero
            movie.save()


        tipo = request.POST.get("tipo")
        if tipo is not None:
         movie.tipoMovie=tipo
         movie.save()

        d=[]
        id_list=[]
        for key in request.POST:
           
            if key.startswith("directores") and ( key is not None) and (key != "") :
               
                dir=request.POST.get(key).split(" ") 
                if dir[0] != "":
                    nombreD=dir[0]
                    apellidoD=dir[1]
                    id= key.split("_")
                    id=id[2]
                    id_list.append(id)
                    try:
                        director = Director.objects.get(nombre=nombreD, apellido=apellidoD)
                        d.append(director)
                    except Director.DoesNotExist:
                        raise    Http404("ERROR DIRECTOR")   


        if d:
            directores=movie.directores.all()
            lista=[]
            count=0
            for a in directores:
                lista.append(a.nombre+" "+a.apellido)
            for i in id_list:
                a = Director.objects.get(nombre=d[count].nombre)
                print(a)
                lista[int(i)-1] = a.nombre+" "+ a.apellido
                count=count+1
            movie.directores.set( nameToSet(lista) )
            print(nameToSet(lista))
            movie.save()
 
        return redirect(reverse('index'))
    

def nameToSet(t):
 lis=[]
 print(t)
 for elemento in t:
    nombres=elemento.split(" ")
    s=Director.objects.get(nombre=nombres[0], apellido=nombres[1])
    lis.append(s)
 print(lis)
 return lis

def reserva(request):
    usuario = request.POST.get("nombre")
    correo = request.POST.get("email")
    fecha = request.POST.get("fecha")
    pelisAcc = request.POST.get("accion")
    pelisH = request.POST.get("historica")
    pelisA = request.POST.get("animacion")
    pelisD = request.POST.get("drama")
    pelisT = request.POST.get("thriller")


    coments = request.POST.get("comentarios","")
    reserva= Reserva(
        usuario=usuario,
        correo=correo,
        fecha=fecha,
        comentarios=coments 
    )
    reserva.save()

    pelis=[]
    p=[]
    a=[pelisA,pelisH,pelisD,pelisT,pelisAcc]
    pelis.extend(a)
    for genero in pelis :
            if genero!= "" and genero is not None:
                try:
                    movie = Movie.objects.get(nombre=genero)  # Adjust the field accordingly
                    p.append(movie)
                except Movie.DoesNotExist:
                 raise Http404("error")
    reserva.peliculas.set( p)
    reserva.save()


    return redirect(reverse("index"))

