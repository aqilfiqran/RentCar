from django.contrib import admin
from django.urls import path, include
from .views import Submit, Index,  SewaListView, SewaCreateView, CarDeleteView, CarCreateView, CarDetailView, CarListView, CarUpdateView

app_name = 'car'
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('<str:pk>/<int:page>/', CarListView.as_view(), name='list'),
    path('create/', CarCreateView.as_view(), name='create'),
    path('sewa/<int:pk>', SewaCreateView.as_view(), name='sewa'),
    path('sewa/list/<int:pk>/<int:page>/',
         SewaListView.as_view(), name='sewalist'),
    path('update/<int:pk>', CarUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', CarDeleteView.as_view(), name='delete'),
    path('detail/<slug:slug>/', CarDetailView.as_view(), name='detail'),
    path('submit/sewa/<int:pk>/', Submit.as_view(), name='submit'),
]
