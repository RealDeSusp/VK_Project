from django.urls import path
from .views import *
from .views import UserCreateAPIView


urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('register_API/', UserCreateAPIView.as_view(), name='register_API'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutUser.as_view(), name='logout'),
]
