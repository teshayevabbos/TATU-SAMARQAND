from django.urls import path
from .views import *

urlpatterns = [
    path('team/',TeamView,name='team'),
]