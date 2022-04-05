from unicodedata import name
from django.db import models

class blog(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=100)
