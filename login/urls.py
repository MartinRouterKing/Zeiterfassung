from django.urls import path
from django.contrib.auth import views

urlpatterns = [
path('', views.login, name='first'),
path('accounts/password_reset', views.login, name='first'),
    ]
