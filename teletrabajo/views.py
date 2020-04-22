#from django.http import HttpResponse 1era opción
from django.shortcuts import render # 2da opción

def hello_world(request):
    #return HttpResponse("Hola Mundo") 1era opción
    return render(request, 'templates/home.html') # 2da opción
