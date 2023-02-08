# Create your models here.
# models.py
from django.db import models


class Youtube(models.Model):
    url = models.CharField(max_length=60)

    def __str__(self):
        return self.url
