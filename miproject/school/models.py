from datetime import date
from unicodedata import name
from django.db import models

# Create your models here.
class commoninfo(models.Model):
    name = models.CharField(max_length=70)
    age = models.IntegerField()
    date = models.DateField()
    class Meta:
        abstract=True


class Student(commoninfo):
    fees = models.IntegerField()
    date = None

class teacher(commoninfo):
    salary = models.IntegerField()