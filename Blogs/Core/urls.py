from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static 
from Core.views import *

urlpatterns = [
    path('', home, name='home'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
