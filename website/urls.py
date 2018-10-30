from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views
#from login.forms import LoginForm




urlpatterns = [
    path('',include('login.urls'), name='home'),
    path('home/', include('datavis.urls')),
    path('admin/', admin.site.urls),
    path('overview/', include('tracking.urls'),name = 'overview'),
    path('input/', include('timetracking.urls'), name='input'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('options/', include('options.urls'), name='options'),
    path('calendar/', include('calender.urls'), name='calendar'),
]

