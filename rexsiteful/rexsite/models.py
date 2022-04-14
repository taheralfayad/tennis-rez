from datetime import datetime, date
from email.policy import default
from django.db import models
from django.conf import settings

# Create your models here.
class Courts(models.Model):
    courtname = models.CharField(max_length=30)

    def __str__ (self):
        return f"{self.courtname}"


class Reservation(models.Model):
    firstname = models.CharField(max_length=40, default="john")
    lastname = models.CharField(max_length=40, default="doe")
    court = models.ForeignKey(Courts, on_delete=models.CASCADE, related_name="court", default= 1)
    dayof = models.DateField(default = date.today())
    starttime = models.TimeField(default = "14:30")
    endtime = models.TimeField(default = "14:30")

    def __str__(self):
        return f"{self.firstname} {self.court}"