from django.db import models
from uuid import uuid4

from .choices import OPERACIONES_INVENTARIO, CITIES
# Create your models here.


class Proveedor(models.Model):
    uuid =  models.UUIDField(primary_key=True, unique=True, default=uuid4, verbose_name='UUID')
    rtn =  models.CharField(max_length=14, verbose_name='RTN', help_text='Ingrese el RTN del proveedor')
    name =  models.CharField(max_length=150, verbose_name='Nombre', help_text='Ingrese el nombre del proveedor')
    city =  models.CharField(max_length=4, choices=CITIES, verbose_name='Ciudad', help_text='Seleccione la ciudad del proveedor')
    address =  models.CharField(max_length=255, verbose_name='Direccion', help_text='Ingrese la direccion del proveedor')
    email  =  models.CharField(max_length=70, verbose_name='Correo Electrónico', help_text='Ingrese el correo electronico del proveedor')
    phone =  models.CharField(max_length=8, verbose_name='Telefono', help_text='Ingrese el correo del proveedor')
    status =  models.BooleanField(default=True, verbose_name='Estado', help_text='Seleccione el estado del proveedor')
    createdAt =  models.DateTimeField(auto_now_add=True)
    updatedAt =  models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name} | {self.rtn}"


class Producto(models.Model):
    uuid =  models.UUIDField(primary_key=True, unique=True, default=uuid4, verbose_name="UUID")
    name =  models.CharField(max_length=200, verbose_name="Nombre")
    price =  models.IntegerField(verbose_name="Precio")
    provider =  models.ForeignKey(Proveedor, on_delete=models.CASCADE, verbose_name="Proveedor")
    status =  models.BooleanField(default=True, verbose_name='Estado', help_text='Seleccione el estado del proveedor')
    createdAt =  models.DateTimeField(auto_now_add=True)
    updatedAt =  models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}"


class Operacion(models.Model):
    uuid =  models.UUIDField(primary_key=True, unique=True, default=uuid4, verbose_name="UUID")
    description = models.CharField(max_length=200, verbose_name='Descripcion', help_text='Ingrese la descripcion')
    product = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name="Producto")
    quantity = models.IntegerField(verbose_name='Cantidad', help_text='Seleccione la cantidad de la operacion')
    type = models.CharField(max_length=2, choices=OPERACIONES_INVENTARIO, verbose_name='Tipo', help_text='Ingrese el tipo de operacion')
    status =  models.BooleanField(default=True, verbose_name='Estado', help_text='Seleccione el estado del proveedor')
    createdAt =  models.DateTimeField(auto_now_add=True)
    updatedAt =  models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.product} | {self.type}"
    
    def get_type_name(self) -> str:
        for type in OPERACIONES_INVENTARIO:
            if type[0] == self.type:
                return type[1]











     
    

