
from django.urls import path, include
from django.contrib import admin
from . import views

admin.autodiscover()

urlpatterns = [
    # Examples:
    path('', views.all_events, name='calendar'),
    path('post/', views.postview, name='postview'),
    path('load_elements/', views.load_elements, name='load_elements')
    #path('all_events/', views.all_events, name='all_events'),
]
