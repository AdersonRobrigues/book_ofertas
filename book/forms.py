from django import forms
from .models import BookCompra, BookVenda, BookCompraMerc, BookVendaMerc
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
   
class CadOfertaC(forms.ModelForm):
    class Meta:
        model = BookCompra
        fields = '__all__'

class CadOfertaV(forms.ModelForm):
    class Meta:
        model = BookVenda
        fields = '__all__'


class CadOfertaCoMer(forms.ModelForm):
    class Meta:
        model = BookCompraMerc
        fields = '__all__'


class CadOfertaVeMer(forms.ModelForm):
    class Meta:
        model = BookVendaMerc
        fields = '__all__'
