from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registrar_propietario/', views.registrar_propietario, name='registrar_propietario'),
    path('listar_propietarios/', views.listar_propietarios, name='listar_propietarios'),
    path('editar_propietario/<int:id>/', views.editar_propietario, name='editar_propietario'),
    path('eliminar_propietario/<int:id>/', views.eliminar_propietario, name='eliminar_propietario'),
    path('registrar_vehiculo/', views.registrar_vehiculo, name='registrar_vehiculo'),
    path('listar_vehiculos/', views.listar_vehiculos, name='listar_vehiculos'),
    path('editar_vehiculo/<int:id>/', views.editar_vehiculo, name='editar_vehiculo'),
    path('eliminar_vehiculo/<int:id>/', views.eliminar_vehiculo, name='eliminar_vehiculo'),
    path('registrar_registro/', views.registrar_registro, name='registrar_registro'),
    path('listar_registros/', views.listar_registros, name='listar_registros'),
    path('detalle_propietario/<int:id>/', views.detalle_propietario, name='detalle_propietario'),
    path('detalle_vehiculo/<int:id>/', views.detalle_vehiculo, name='detalle_vehiculo'),
    path('registros/', views.listar_registros, name='listar_registros'),
    path('registro/<int:pk>/', views.detalle_registro, name='detalle_registro'),
    path('registro/<int:pk>/editar/', views.editar_registro, name='editar_registro'),
    path('registro/<int:pk>/eliminar/', views.eliminar_registro, name='eliminar_registro'),
]
