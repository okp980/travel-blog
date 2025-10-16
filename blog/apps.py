from django.apps import AppConfig
from django.db.models.signals import post_save



class BlogConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "blog"

    def ready(self):
        import blog import signals
        
        post_save.connect(signals.create_post_slug, sender=Posts)
        post_save.connect(signals.create_destination_slug, sender=Destinations)
