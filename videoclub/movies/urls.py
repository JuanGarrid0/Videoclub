from django.contrib import admin
from django.urls import include, path
from movies import views

urlpatterns = [
    path('', views.index, name ="index"),
    path('director', views.director, name="director"),
    path('genero', views.genero, name="genero"),
    path('lista', views.lista, name="lista"),
    path("formulario", views.formulario, name="formulario"),
    path('detalles/<str:tipo>/<str:nombre>/',views.detalles, name="detalles"),
    path('buscarDirector/', views.buscarDirector, name='buscarDirector'),
    path("login", views.login_view, name="login"),
    path("register", views.register, name="register"),
    path("logout", views.logout_view, name="logout"),
    path("delete/<str:peli>", views.delete, name="delete"),
    path("updatePage/<str:peli>", views.updatePage, name="updatePage"),
    path("update/<int:peli>", views.update, name="update"),
    path("BuscarPeliculas/", views.buscarPeliculas, name="BuscarPeliculas"),
    path("reserva/", views.reserva, name="reserva"),

]
