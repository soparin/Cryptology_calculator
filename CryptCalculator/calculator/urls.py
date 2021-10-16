from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('<str:algo>/', algorithm),
    path('euclid/', euclidIndex),
    path('sundaram/', sundaramIndex),
]