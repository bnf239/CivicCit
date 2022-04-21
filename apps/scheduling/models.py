from enum import unique
from django.db import models #create models

class Event(models.Model):
    event_name = models.CharField(max_length=500,default=None)
    event_location =  models.CharField(max_length=500,default=None)
    event_date =  models.DateTimeField(default=None)
    event_link =  models.CharField(max_length=500, unique=True,default=None)
    event_status = models.BooleanField(default=False)