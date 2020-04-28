from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views
from .views import ReporteTareaExcel

urlpatterns = [
    path('', views.tareas_lista, name="tareas_lista"),
    #path('reporte_excel_tarea', views.ReporteTareaExcel, name="reporte_excel_tarea"),
    url(r'^reporte_excel_tarea/', login_required(ReporteTareaExcel.as_view()), name = "reporte_excel_tarea"),
]
