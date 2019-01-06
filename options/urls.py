from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('ajax/load-element/', views.load_elements, name='ajax_load_element'),
    path('', views.options, name='options'),
    path('addfavorites/', views.addfavortites, name='addfavorites'),
    path('admin_options/addcategories/', views.addcategories, name='add_cat'),
    path('admin_options/editcategories/', views.editcategories, name='edit_cat'),
    path('admin_options/deletecategories/', views.deletecategories, name='del_cat'),
    path('admin_options/adduser/', views.create_user, name='create_user'),

    path('admin_options/addelements/', views.addelements, name='add_ele'),
    path('admin_options/editelements/', views.editelements, name='edit_ele'),
    path('admin_options/deleteelements/', views.deleteelements, name='del_ele'),

    path('load_favorites/', views.load_favorites, name='load_favorites'),
    path('admin_options/', views.admin_options, name='admin_options'),
    path('admin_options/load_elements/', views.load_favelements, name='load_elements'),
    path('admin_options/load_fav/', views.load_fav, name='load_fav'),
    path('admin_options/load_combination/', views.load_combination, name='load_combination'),
    path('admin_options/load_categorie/', views.load_categorie, name='load_categorie'),
    path('admin_options/ajax_table/', views.ajax_table, name='ajax_table'),
    path('admin_options/addcalc/', views.addcalc, name='add_calc'),
]
