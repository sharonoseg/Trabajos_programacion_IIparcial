from django.db import models
from uuid import uuid4

# Create your models here.


class Persona(models.Model):
    uuid =  models.UUIDField(primary_key=True, unique=True, default=uuid4)
    dni = models.CharField(max_length=13, unique=True)
    firstname =  models.CharField(max_length=50)
    lastname =  models.CharField(max_length=50)
    bornday =  models.DateField()
    status =  models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)


class Cargo(models.Model):
    uuid =  models.UUIDField(primary_key=True, unique=True, default=uuid4)
    name = models.CharField(max_length=100)
    status =  models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)


class Cliente(models.Model):
    uuid =  models.UUIDField(primary_key=True, unique=True, default=uuid4)
    person =  models.ForeignKey(Persona, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=8)
    status =  models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)


class Usuario(models.Model):
    uuid =  models.UUIDField(primary_key=True, unique=True, default=uuid4)
    person =  models.ForeignKey(Persona, on_delete=models.CASCADE)
    position =  models.ForeignKey(Cargo, on_delete=models.CASCADE)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=8)
    status =  models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)


