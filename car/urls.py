from django.contrib import admin
from django.urls import path, include
from .views import SewaListView, SewaCreateView, CarDeleteView, CarCreateView, CarDetailView, CarListView, index, CarUpdateView

app_name = 'car'
urlpatterns = [
    path('', index, name='index'),
    path('<str:pk>/<int:page>/', CarListView.as_view(), name='list'),
    path('create/', CarCreateView.as_view(), name='create'),
    path('sewa/<int:pk>', SewaCreateView.as_view(), name='sewa'),
    path('sewa/list/<int:page>',
         SewaListView.as_view(), name='sewalist'),
    path('update/<int:pk>', CarUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', CarDeleteView.as_view(), name='delete'),
    path('detail/<slug:slug>/', CarDetailView.as_view(), name='detail')
]
