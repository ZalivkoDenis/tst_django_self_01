from django.db import models


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=100, null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
