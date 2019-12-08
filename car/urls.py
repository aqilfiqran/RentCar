from django.contrib import admin
from django.urls import path, include
from .views import index, CarCreateView, CarDetailView

app_name = 'car'
urlpatterns = [
    path('', index, name='index'),
    path('create/', CarCreateView.as_view(), name='create'),
    path('detail/<slug:slug>/', CarDetailView.as_view(), name='detail')
]
