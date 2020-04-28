from django.shortcuts import render
#from django.http import HttpResponse 1era opción

#from openpyxl import Workbook
#from django.http.response import HttpResponse
#from django.views.generic import TemplateView

from .models import Tarea

def tareas_lista(request):
    tareas = Tarea.objects.all()

    #response = ', '.join([str(tarea) for tarea in tareas]) 1era opción
    #return HttpResponse(response) 1era opción
    return render(request, 'tareas/tareas_lista.html', {'tareas':tareas}) # 2da opción

# class ReporteTareaExcel(TemplateView):
#     def get(self, request, *args, **kwargs):
#         tareas = Tarea.objects.all()
#         wb = Workbook()
#         ws = wb.active
#         ws['B1'] = 'REPORTE DE TAREAS'
#         ws.merge_cells('B1:E1')
#         ws['B3'] = 'fechaCreacion'
#         ws['C3'] = 'titulo'
#         ws['D3'] = 'descripcion'
#         ws['E3'] = 'comentarios'
#
#         cont = 4
#
#         for t in tareas:
#             ws.cell(row = cont, column = 2).value = t.fechaCreacion
#             ws.cell(row = cont, column = 3).value = t.titulo
#             ws.cell(row = cont, column = 4).value = t.descripcion
#             ws.cell(row = cont, column = 5).value = t.comentarios
#             cont += 1
#         nombre_archivo = "ReporteTareaExcel.xlsx"
#         response = HttpResponse(content_type = "application/ms-excel")
#         content = "attachment; filename = {0}".format(nombre_archivo)
#         response['Content-Disposition'] = content
#         wb.save(response)
#         return response
