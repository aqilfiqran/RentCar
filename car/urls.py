from django.contrib import admin
from django.urls import path, include
from .views import index

app_name = 'car'
urlpatterns = [
    path('', index, name='indexcar'),
]
