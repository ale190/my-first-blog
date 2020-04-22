from django.shortcuts import render
#from django.http import HttpResponse 1era opción

from .models import Tarea

def tareas_lista(request):
    tareas = Tarea.objects.all()
    #response = ', '.join([str(tarea) for tarea in tareas]) 1era opción
    #return HttpResponse(response) 1era opción
    return render(request, 'tareas/TAREAS_LISTA.html', {'tareas':tareas}) # 2da opción
