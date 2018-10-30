from django.urls import path
from . import views

urlpatterns = [
    #path('', views.tracking, name='overview'),
    path('', views.input, name='input'),
    path('ajax/load-element/', views.load_elements, name='ajax_load_element'),
]


