from django.urls import path
from .views import *

urlpatterns = [
    path('facturas/', ObtenerFacturas.as_view(), name = 'listar_facturas'),
    path('factura/add', AgregarFactura.as_view(), name='agregar_factura'),
]