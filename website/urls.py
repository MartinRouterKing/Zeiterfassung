from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('',include('login.urls'), name='home'),
    path('home/', include('datavis.urls')),
    path('admin/', admin.site.urls, name='admin'),
    path('overview/', include('tracking.urls'),name = 'overview'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('options/', include('options.urls'), name='options'),
    path('calendar/', include('calender.urls'), name='calendar'),
    path('acc/', include('accounting.urls'), name='accounting'),
    path('controlling/', include('controlling.urls'), name='controlling'),

]

