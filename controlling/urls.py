from django.urls import path
from . import views
urlpatterns = [
    path('', views.ControllingView, name='controlling'),
    path('controlling/search/', views.search, name='search'),
    path('controlling/search_line/', views.search_line, name='search_line'),

]
