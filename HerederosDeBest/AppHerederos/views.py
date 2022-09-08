from django.shortcuts import render
from django.template import loader
from urllib import request 

# Create your views here.
def Integrantes(request):
    return render(request, 'AppHerederos/integrantes.html')

def ProximasFechas(request):
    return render(request, 'AppHerederos/proximasfechas.html')

def Lugares(request):
    return render(request, 'AppHerederos/lugares.html')

def Anecdotas(request):
    return render(request, 'AppHerederos/anecdotas.html')

