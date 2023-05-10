from django.urls import path, include
from django.contrib import admin
from .yasg import urlpatterns as doc_urls


# ссылки на главную страницу и панель администратора
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('social_network.urls')),
]

# для работы openAPI
urlpatterns += doc_urls
