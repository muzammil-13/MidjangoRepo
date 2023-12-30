from django.db import models
from django.urls import reverse
from django.db.models.base import Model
from django.db.models.deletion import CASCADE


class Department(models.Model):
    departmentname = models.CharField(max_length=100)




class Course(models.Model):
    deptid = models.ForeignKey(Department, on_delete=CASCADE)
    crsename = models.CharField(max_length=100)

