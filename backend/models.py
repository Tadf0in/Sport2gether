from django.db import models
from django.contrib.auth.models import User


class Sport(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name