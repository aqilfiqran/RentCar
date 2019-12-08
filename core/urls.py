from django.contrib import admin
from django.urls import path, include
from .views import UserFormView, LoginView, LogoutView

app_name = 'car'
urlpatterns = [
    path('register/', UserFormView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView, name='logout'),
]
