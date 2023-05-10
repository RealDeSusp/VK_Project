from django.urls import path, include
from .views import *

# ссылки на страницы приложения social_network
urlpatterns = [
    path('', index, name='index'),
    path('friend-list/', friend_list, name='friend_list'),
    path('friendship/', include('friendship.urls')),
    path('register/', register, name='register'),
    path('register_API/', UserCreateAPIView.as_view(), name='register_API'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutUser.as_view(), name='logout'),
]
