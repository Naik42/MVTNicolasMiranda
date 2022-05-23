from django.urls import path
from django.urls import URLPattern
from . import views




urlPatterns = [

    path("", views.inicio),
    path("lista_familiares", views.lista_familiares),
    path("alta_familiares", views.altaF),



]