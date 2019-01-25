from django.db import models
from django.dispatch import receiver
from django.urls import reverse

from links.utils import unique_slug_generator


class Link(models.Model):
    slug = models.SlugField(blank=True, unique=True)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('link', kwargs={'slug': self.slug})


@receiver(models.signals.pre_save, sender=Link)
def add_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
