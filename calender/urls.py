from django.urls import path, include
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

from .tasks import notify_user
from background_task.models import Task
from django.core.exceptions import ObjectDoesNotExist

try:
    task_list = Task.objects.all()
except ObjectDoesNotExist:
    check = None
    notify_user(repeat=Task.DAILY)
else:
    Task.objects.all().delete()
    notify_user(repeat=Task.DAILY)


urlpatterns = [
    path('', views.all_events, name='calendar'),
    path('post/', views.postview, name='postview'),
    path('load_elements/', views.load_elements, name='load_elements')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
