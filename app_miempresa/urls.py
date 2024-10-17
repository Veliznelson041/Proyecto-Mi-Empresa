

from django.urls import path
from app_miempresa import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listado/', views.listado, name='listado'),
    path('', views.index, name='index'),
    path('nuevo_cliente/', views.nuevo_cliente, name='nuevo_cliente'),
    path('editar_cliente/<int:id>/', views.editar_cliente, name='editar_cliente'),  # Ruta para editar cliente
]
