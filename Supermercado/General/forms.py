from django import forms
from .models import *

class AddCargoForm(forms.Form):
    name = forms.CharField(max_length=100, label='Nombre del Cargo', widget=forms.TextInput(attrs={'class':'form-control'}))



class UpdateCargoForm(forms.ModelForm):
    name = forms.CharField(max_length=100, label='Nombre del cargo', widget=forms.TextInput(attrs={'class':'form-control'}))


    class Meta:
        model = Cargo
        fields = ['name']

class AddClientesForm(forms.Form):
    person = forms.ModelChoiceField(queryset=Cliente.objects.all(),label="Persona",widget=forms.Select(attrs={'class':'form-select'}))
    address = forms.CharField(max_length=255,label="Direccion",widget=forms.Textarea(attrs={'class':'form-control'}))
    phone = forms.CharField(max_length=8,label="Telefono",widget=forms.TextInput(attrs={'class':'form-control'}))


     