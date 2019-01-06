from django.urls import path
from . import views
urlpatterns = [
    path('', views.Analyticsview, name='home'),
    path('load_canvas/', views.load_canvas, name='load_canvas'),
    path('load_bar_cat/', views.load_bar_cat, name='load_bar_cat')
]
