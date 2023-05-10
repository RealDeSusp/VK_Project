from django.apps import AppConfig


# создание приложения для реализации социальной сети
class SocialNetworkConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'social_network'
