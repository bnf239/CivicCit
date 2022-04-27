from django.db import models
from django.contrib.auth.models import User
 
# Create your models here.
class QuizCategoryModel(models.Model):

    CATEGORY_CHOICES = (
        ('P', 'Political Involvement'),
        ('S', 'Social Responsibility'),
        ('C', 'Commmunity Service'),
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.CharField(max_length=1,choices=CATEGORY_CHOICES,null=False)
    numRight = models.IntegerField(null=True)
    totalQuestions = models.IntegerField(default=10)
    percent = models.FloatField(null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.category