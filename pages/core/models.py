from django.db import models


class Books(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_at = models.DateField(blank=True)

    def __str__(self):
        return self.title
