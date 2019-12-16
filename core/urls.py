from django.contrib import admin
from django.urls import path, include
from .views import EditProfil,UserFormView, LoginView, LogoutView

app_name = 'core'
urlpatterns = [
    path('edit/<int:pk>', EditProfil.as_view(), name='profiledit'),
    path('register/', UserFormView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView, name='logout'),
]
