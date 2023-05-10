from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView
from .forms import RegistrationForm
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from .serializers import UserSerializer
from friendship.models import Friend


def index(request):
    return render(request, template_name='social_network/base.html')


@login_required(login_url="/social_network/login/")
def friend_list(request):
    # Получаем список друзей текущего пользователя
    friends = Friend.objects.friends(request.user)
    print(friends)
    # Возвращаем шаблон и передаем список друзей в контекст
    return render(request, template_name='social_network/friend_list.html', context={'friends': friends})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RegistrationForm()
    return render(request, template_name='social_network/register.html', context={'form': form})


class LoginUser(LoginView):
    template_name = 'social_network/login.html'

    def get_success_url(self):
        return reverse_lazy('index')


class LogoutUser(LogoutView):
    def get_success_url(self):
        return reverse_lazy('index')


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]