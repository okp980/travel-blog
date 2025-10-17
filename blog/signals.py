from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from blog.models import Post


@receiver(post_save, sender=Post)
def create_post_slug(sender, instance, created, **kwargs):
    if created:
        instance.slug = slugify(instance.title)
        instance.save()
