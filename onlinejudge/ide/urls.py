from django.urls import path

from . import views

urlpatterns = [
    path('MINIMUMJUMPS/code', views.code, name = 'code'),
]