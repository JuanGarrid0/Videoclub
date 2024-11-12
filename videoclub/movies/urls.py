from django.contrib import admin
from django.urls import include, path
from movies import views

urlpatterns = [
    path('', views.index, name ="index"),
    path('director', views.director, name="director"),
    path('genero', views.genero, name="genero"),
    path('lista', views.lista, name="lista"),
    path('detalles',views.detalles, name="detalles"),

]
