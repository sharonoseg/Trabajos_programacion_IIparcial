from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View
from .models import *
from .forms import *

# Create your views here.

class ObtenerCargos(View):
    def get(self, request):
        cargos = Cargo.objects.all()

        return render(request, 'cargos/listar_cargos.html',{'cargos':cargos})
    
class AgregarCargo(View):
        def get(self, request):
            form = AddCargoForm()
            return render(request, 'cargos/agregar_cargo.html', {'form':form})

        def post(self,request):
            form = AddCargoForm(request.POST)

            if(form.is_valid()):
                obj = Cargo()
                obj.name = form.cleaned_data['name']
                obj.save()

                return HttpResponseRedirect(reverse('listar_cargos'))
            
class ActualizarCargo(View):
        def get(self, request, uuid):
             obj = Cargo.objects.get(uuid=uuid)
             form = UpdateCargoForm(instance=obj)
             
                
             return render(request, 'cargos/agregar_cargo.html', {'form':form})
             
        def post(self, request, uuid):
            obj = Cargo.objects.get(uuid=uuid)
            form = UpdateCargoForm(request.POST, instance=obj)

            if(form.is_valid()):
               obj = form.save(commit=False)
               obj.save()
         
class ObtenerClientes(View):
    def get(self, request):
        clientes = Cliente.objects.all()

        return render(request, 'clientes/listar_clientes.html',{'clientes':clientes})
    

class ObtenerUsuarios(View):
    def get(self, request):
        usuarios = Usuario.objects.all()

        return render(request, 'usuarios/listar_usuarios.html',{'usuarios':usuarios})

class AgregarClientes(View):
    def get(self, request):
        form = AddClientesForm()
        return render(request, 'clientes/agregar_clientes.html', {'form':form})

    def post(self,request):
        form = AddClientesForm(request.POST)

        if(form.is_valid()):
            obj = Cliente()
            obj.name = form.cleaned_data['name']
            obj.save()

            return HttpResponseRedirect(reverse('listar_clientes'))
        
class Agregarusuarios(View):
    def get(self, request):
        form = AddusuariosForm()
        return render(request, 'clientes/agregar_usuarios.html', {'form':form})

    def post(self,request):
        form = AddusuariosForm(request.POST)

        if(form.is_valid()):
            obj = usuarios()
            obj.name = form.cleaned_data['name']
            obj.save()

            return HttpResponseRedirect(reverse('listar_usuarios'))