from django.db import models
from General.models import *
from Inventario.models import *
from uuid import uuid4

from .choices import ESTADO_DE_PAGO

# Create your models here.


class Factura(models.Model):
    uuid =  models.UUIDField(verbose_name='UUID', primary_key=True, unique=True, default=uuid4)
    client =  models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name='Cliente')
    rtn =  models.CharField(max_length=14, verbose_name='RTN', blank=True)
    paymentStatus =  models.CharField(max_length=2, choices=ESTADO_DE_PAGO, verbose_name='Estado de Pago', default='0')
    status =  models.BooleanField(default=True, verbose_name='Estado')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)


class ElementoFactura(models.Model):
    uuid =  models.UUIDField(verbose_name='UUID', primary_key=True, unique=True, default=uuid4)
    product =  models.ForeignKey(Producto,  on_delete=models.CASCADE, verbose_name='Producto')
    quantity =  models.IntegerField(verbose_name='Cantidad', default=1)
    invoice =  models.ForeignKey(Factura, on_delete=models.CASCADE, verbose_name='Factura')
    status =  models.BooleanField(default=True, verbose_name='Estado')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)