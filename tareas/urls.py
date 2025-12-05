# tareas/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('', views.lista_tareas, name='lista_tareas'),
    path('tarea/<int:indice>/', views.detalle_tarea, name='detalle_tarea'),
    path('tarea/nueva/', views.agregar_tarea, name='agregar_tarea'),
    path('tarea/<int:indice>/eliminar/', views.eliminar_tarea, name='eliminar_tarea'),
]
