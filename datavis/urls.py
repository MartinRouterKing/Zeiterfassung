from django.urls import path
from . import views
urlpatterns = [
    path('', views.Analyticsview, name='home'),
    path('load_canvas/', views.load_canvas, name='load_canvas')
]
