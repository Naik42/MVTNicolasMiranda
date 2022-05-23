from django.http import HttpResponse
from django.shortcuts import render
from usuarios.models import Familiares
from django.http import HttpResponse



def inicio(request):
    return render( request , "index.html")



def lista_familiares(request):
    familiares = Familiares.objects.all()
    datos = { "datos" : familiares}

    return render (request , "lista_familiares.html" , datos)



def altaF(request):
    familiar = Familiares ( nombre = "Nahuel" , edad=26 , nacimiento= "1993-1-17")
    familiar.save()
    familiar = Familiares ( nombre = "Alma" , edad=19 , nacimiento= "2003-4-23")
    familiar.save()
    familiar = Familiares ( nombre = "Gloria" , edad=49 , nacimiento= "1973-4-17")
    familiar.save()

    return HttpResponse("Alta dada")