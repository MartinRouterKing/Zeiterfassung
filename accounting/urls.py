from django.urls import path
from django.contrib import admin
from . import views

admin.autodiscover()

urlpatterns = [
    path('', views.accounting, name='accounting'),
    path('table/', views.ajaxtable, name='table')
    ]
