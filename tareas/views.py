from django.shortcuts import render
from django.http import HttpResponse

from .models import Tarea

def tareas_lista(request):
    tareas = Tarea.objects.all()
    #response = ', '.join([str(tarea) for tarea in tareas]) 1era opción
    #return HttpResponse(response) 1era opción
    return render(request, 'tareas/tareas_lista.html', {'tareas':tareas}) # 2da opción
