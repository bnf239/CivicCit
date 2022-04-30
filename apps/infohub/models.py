from django.db import models
from django.contrib.auth.models import User

# Create models 

class InfoHubUserInformation(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    article_title = models.CharField(max_length=1000, default="Some string")
    url_links = models.CharField(max_length=1000)
