from django.urls import path
from . import views
urlpatterns = [
    path('', views.Analyticsview, name='home'),
]
