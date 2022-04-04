from django.db import models #create models

class Event(models.Model):
    event_name = models.CharField(max_length=500)
    event_location =  models.CharField(max_length=500)
    event_date =  models.DateTimeField()
    event_link =  models.CharField(max_length=500)