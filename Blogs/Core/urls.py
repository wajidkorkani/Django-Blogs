from django.urls import path 
from Core.views import *

urlpatterns = [
    path('', home, name='home'),
]
