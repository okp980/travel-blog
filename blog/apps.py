from django.apps import AppConfig
from django.db.models.signals import post_save


class BlogConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "blog"

    def ready(self):
        from . import signals

        post_save.connect(signals.create_post_slug)
