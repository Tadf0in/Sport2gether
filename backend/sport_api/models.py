from django.db import models


class Sport(models.Model):
    name = models.CharField(max_length=128, unique=True)
    icon_url = models.URLField(max_length=128, blank=True)

    def __str__(self):
        return self.name
