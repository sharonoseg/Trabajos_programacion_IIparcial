from django.shortcuts import render
from django.views import View
from .forms import *
from .models import *

# Create your views here.

class ObtenerFacturas(View):
    def get(self, request):
        facturas = Factura.objects.all()

        return render(request, 'facturas/listar_facturas.html', {'facturas':facturas})

class AgregarFactura(View):
    def get(self, request):
        form = AddFacturaForm()

        return render(request, 'factura/agregar_factura.html', {'facturas': form})

