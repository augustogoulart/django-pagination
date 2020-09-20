from django.db import models

from pages.core.managers import PageManager


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_at = models.DateField()

    objects = PageManager()

    def __str__(self):
        return self.title
