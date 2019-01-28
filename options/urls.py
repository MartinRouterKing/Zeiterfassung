from django.urls import path,re_path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('ajax/load-element/', views.load_elements, name='ajax_load_element'),
    path('', views.options, name='options'),
    path('addfavorites/', views.addfavortites, name='addfavorites'),
    path('admin_options/addcategories/', views.addcategories, name='add_cat'),
    path('admin_options/editcategories/', views.editcategories, name='edit_cat'),
    path('admin_options/deletecategories/', views.deletecategories, name='del_cat'),


    path('admin_options/addelements/', views.addelements, name='add_ele'),
    path('admin_options/editelements/', views.editelements, name='edit_ele'),
    path('admin_options/deleteelements/', views.deleteelements, name='del_ele'),

    path('load_favorites/', views.load_favorites, name='load_favorites'),
    path('admin_options/', views.admin_options, name='admin_options'),
    path('admin_options/load_elements/', views.load_favelements, name='load_elements'),
    path('admin_options/load_fav/', views.load_fav, name='load_fav'),

    path('admin_options/ajax_save_element/', views.ajax_save_element, name='ajax_save_element'),
    path('admin_options/ajax_add_from_group/', views.ajax_add_from_group, name='ajax_add_from_group'),
    path('admin_options/ajax_load_from_groups/', views.ajax_load_from_groups, name='ajax_load_from_groups'),
    path('admin_options/addcalc/', views.addcalc, name='add_calc'),
    path('admin_options/editcalc/', views.editcalc, name='editcalc'),
    path('admin_options/deletecalc/', views.deletecalc, name='deletecalc'),
    path('admin_options/edit_user/',views.edit_user, name='edit_user'),
    path('admin_options/ajax_load_userdata/',views.ajax_load_userdata, name='ajax_load_userdata'),
]

