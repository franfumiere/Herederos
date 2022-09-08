from django.contrib import admin
from django.urls import path 
from AppHerederos.views import *

urlpatterns = [
    path('integrantes/', Integrantes, name="Integrantes"),
    path('anecdotas/', Anecdotas, name="Anecdotas"),
    path('lugares/', Lugares, name="Lugares"),
    path('proximasfechas/', ProximasFechas, name="ProximasFechas")
]