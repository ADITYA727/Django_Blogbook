from django.apps import AppConfig


class BlogappConfig(AppConfig):
    name = 'Blogapp'

    def ready(self):
        import Blogapp.signals
