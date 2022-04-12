from django.db import models
import datetime
from django.db.models.base import Model



class Students(models.Model):
    Name = models.CharField(max_length=200)
    RollNo = models.CharField(max_length=6)
    phoneNumber = models.CharField(max_length=10)
    email = models.EmailField(max_length=200 ,null = True)
    def __str__(self):
        return str(self.Name)
    