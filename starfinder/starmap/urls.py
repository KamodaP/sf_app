from django.urls import path

from . import views

urlpatterns = [
    path('', views.galaxy_map, name='galaxymap')
]