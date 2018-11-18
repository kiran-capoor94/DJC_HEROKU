from django.db import models
from django.urls import reverse
from django.conf import settings
from django.db.models.signals import pre_save, post_save

from .utils import unique_slug_generator
from apps.tags.models import Tag

class Gallery(models.Model):
    title = models.CharField(max_length=200)
    alt = models.CharField(max_length=2000)
    gallery_image = models.ImageField(upload_to = "gallery/%Y/%m/%d", blank=True, null=True)
    slug = models.SlugField(blank=True, unique=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return "/Blogs/{slug}/".format(slug=self.slug)
        return reverse("gallery:detail", kwargs={'slug': self.slug})

    class Meta:
        ordering = ('title',)
        verbose_name = 'gallery'
        verbose_name_plural = 'galleries'

def gallery_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(gallery_pre_save_reciever, sender=Gallery)