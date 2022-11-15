from django.urls import path
from django.contrib import admin
from prezents.views import index

urlpatterns = [ 
    path('index/', index, name='index')
]