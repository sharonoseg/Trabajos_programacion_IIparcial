from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View
from .models import *
from.forms import*

# Create your views here.

class ListarProveedores(View):
    def get(self, request):
        proveedores =  Proveedor.objects.all()

        return render(request, "proveedores/listar_proveedores.html", {"proveedores":proveedores})

class AgregarProveedor(View):
    def get(self , request):
        form = AddProveedorForm()

        return render(request, "proveedores/agregar_proveedor.html", {"form":form})
    
    def post(self, request):
        form = AddProveedorForm (request.POST)

        if (form.is_valid()):
            obj = Proveedor()
            obj.rtn  = form.cleaned_data['rtn']
            obj.name = form.cleaned_data['name']
            obj.city = form.cleaned_data['city']
            obj.address = form.cleaned_data['address']
            obj.email = form.cleaned_data['email']
            obj.phone = form.cleaned_data['phone']
            obj.save()

            return HttpResponseRedirect(reverse('listar_proveedores'))
                
class ActualizarProveedor(View):
    def get(self, request, uuid):
        proveedor = Proveedor.objects.get(uuid=uuid)
        form = UpdateProveedorForm(instance=proveedor)

        return render(request, 'proveedores/agregar_proveedor.html',{'form': form})

class ObtenerProveedorPorUUID(View):
    def get(self, request, uuid):
        proveedor =  Proveedor.objects.get(uuid=uuid)
        productos =  Producto.objects.filter(provider=proveedor)

        return render(request, 'proveedores/proveedor_spor_uuid.html', {'proveedor': proveedor, 'productos':productos})


class ListarProductos(View):
    def get(self, request):
        productos =  Producto.objects.all()

        return render(request, "productos/listar_productos.html", {"productos":productos})
    
class AgregarProducto(View):
    def get(self, request):
        form = AddProductoForm()

        return render(request, 'productos/agregar_producto.html', {'form': form})

    def post(self, request):
        form = AddProductoForm(request.POST)

        if(form.is_valid()):
            obj = Producto()
            obj.name = form.cleaned_data['name']
            obj.price = form.cleaned_data['price']
            obj.provider = form.cleaned_data['provider']
            obj.save()

            return HttpResponseRedirect(reverse('listar_productos'))

class ObtenerProductoPorUUID(View):
    def get(self, request, uuid):
        stock = 0
        producto  =  Producto.objects.get(uuid=uuid)
        operaciones =  Operacion.objects.filter(product = producto)
        
        for operacion in operaciones:
            if(operacion.type == '1'):
                stock += operacion.quantity
            elif(operacion.type == '0'):
                stock -= operacion.quantity

        return render(request, 'productos/producto_por_uuid.html', {'producto':producto, 'stock':stock, 'operaciones': operaciones})
    
