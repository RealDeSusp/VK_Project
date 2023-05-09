from django.urls import path, include
from django.contrib import admin
from social_network.views import *
from .yasg import urlpatterns as doc_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('social_network/', include('social_network.urls')),
]

urlpatterns += doc_urls
