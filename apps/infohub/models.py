from django.db import models
from django.contrib.auth.models import User

# Create models 

class InfoHubUserInformation(models.Model):
    username = models.CharField(max_length=1000, blank=True, null=True)
    url_links = models.CharField(max_length=1000)

#     def __str__(self):
#         return self.username