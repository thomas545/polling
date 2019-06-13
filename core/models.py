from django.db import models

# Create your models here.


class TimeStampModel(models.Model):
    created = models.DateTimeField(blank=True, auto_now_add=True)
    updated = models.DateTimeField(blank=True, auto_now=True)
