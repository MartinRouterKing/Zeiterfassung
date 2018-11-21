from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('ajax/load-element/', views.load_elements, name='ajax_load_element'),
    path('', views.options, name='options'),
    path('addcategories/', views.addcategories, name='add'),
    path('addelements/', views.addelements, name='add'),
    path('addfavorites/', views.addfavortites, name='add_fav')
]
