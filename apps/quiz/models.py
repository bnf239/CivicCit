from django.db import models
from django.contrib.auth.models import User
 
# Create your models here.
class QuesModel(models.Model):
    POLITICAL = 'P'
    SOCIAL = 'S'
    COMMUNITY = 'C'

    CATEGORY_CHOICES = (
        (POLITICAL, 'Political Involvement'),
        (SOCIAL, 'Social Responsibility'),
        (COMMUNITY, 'Commmunity Service'),
    )

    question = models.CharField(primary_key=True,max_length=200,null=False,unique=True)
    category = models.CharField(max_length=1,choices=CATEGORY_CHOICES,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)

    def is_political(self):
        return self.category in (self.POLITICAL)

    def is_social(self):
        return self.category in (self.SOCIAL)

    def is_community(self):
        return self.category in (self.COMMUNITY)

    def __str__(self):
        return self.question
    

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