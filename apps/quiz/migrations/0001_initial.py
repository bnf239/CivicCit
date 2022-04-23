from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from quiz import models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    CATEGORY_CHOICES = (
        ('P', 'Political Involvement'),
        ('S', 'Social Responsibility'),
        ('C', 'Commmunity Service'),
    )

    operations = [
        migrations.CreateModel(
            name='QuesModel',
            fields=[
                ('question', models.CharField(max_length=200, primary_key=True, serialize=False, unique=True)),
                ('category', models.CharField(choices=CATEGORY_CHOICES, max_length=1, primary_key=True, serialize=False, unique=True)),
                ('op1', models.CharField(max_length=200,null=True)),
                ('op2', models.CharField(max_length=200,null=True)),
                ('op3', models.CharField(max_length=200,null=True)),
                ('op4', models.CharField(max_length=200,null=True)),
                ('ans', models.CharField(max_length=200,null=True))
            ],
        ),
        migrations.CreateModel(
            name='QuizCategoryModel',
            fields=[
                ('category', models.CharField(max_length=1,choices=CATEGORY_CHOICES,null=False,primary_key=True)),
                ('numRight', models.IntegerField(null=True)),
                ('totalQuestions', models.IntegerField(default=10)),
                ('percent',  models.FloatField(null=True)),
                ('completed', models.BooleanField(default=False))
            ],
        ),
    ]