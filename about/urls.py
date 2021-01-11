from django.urls import path
from . import views
from about.dash_apps.finished_apps import simpleexample

urlpatterns = [
    path('', views.about, name='about')
]
