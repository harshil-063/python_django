from pyexpat import model
from django.db import models

# Create your models here.
class Student(models.Model):
    stuid = models.IntegerField()
    stuname = models.CharField(max_length=70)
    stuemail = models.CharField(max_length=70)
    stupass = models.CharField(max_length=70)

class Employee(models.Model):
    empid = models.IntegerField(primary_key=True,auto_created=True)
    empname = models.CharField(max_length=50)
    empemail = models.CharField(max_length=50)

    # str() is used to display employeename instead of object in admin panel
    # it returns single field name
    def __str__(self):
        return self.empname