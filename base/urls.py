from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskList, name='Tasks')
]