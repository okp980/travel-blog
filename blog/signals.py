from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from .models import Posts


@receiver(post_save, sender=Posts)
def create_post_slug(sender, instance, created, **kwargs):
    if created:
        instance.slug = slugify(instance.title)
        instance.save()


@receiver(post_save, sender=Destinations)
def create_destination_slug(sender, instance, created, **kwargs):
    if created:
        instance.slug = slugify(instance.name)
        instance.save()
