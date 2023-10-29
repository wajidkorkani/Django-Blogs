from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static 
from Core.views import *

urlpatterns = [
    path('', home, name='home'),
    path('searched/', searchbar, name="searchbar"),
    path('about/<slug:slug>/<int:pk>/', about, name='about'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
