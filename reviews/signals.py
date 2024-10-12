from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Review
from django.utils.text import slugify

@receiver(pre_save, sender=Review)
def add_slug(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.movie_title)  
        instance.slug = slug
