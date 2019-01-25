from django.db import models
from django.urls import reverse


class Link(models.Model):
    slug = models.SlugField(blank=True, unique=True)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('link', kwargs={'slug': self.slug})
