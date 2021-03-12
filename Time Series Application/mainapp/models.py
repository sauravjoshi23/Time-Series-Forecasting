from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Item(models.Model):
    Date = models.CharField(max_length=50)
    Sales = models.FloatField()

    def __str__(self):
        return self.Date