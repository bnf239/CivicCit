from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200,null=True)),
                ('category', models.CharField(max_length=1,choices=CATEGORY_CHOICES,null=True)),
                ('op1', models.CharField(max_length=200,null=True)),
                ('op2', models.CharField(max_length=200,null=True)),
                ('op3', models.CharField(max_length=200,null=True)),
                ('op4', models.CharField(max_length=200,null=True)),
                ('answer', models.CharField(max_length=200,null=True))
            ],
        ),
        migrations.CreateModel(
            name='QuizCategoryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=1,choices=CATEGORY_CHOICES,null=True)),
                ('numRight', models.IntegerField(null=True)),
                ('totalQuestions', models.IntegerField(default=10)),
                ('percent',  models.FloatField(null=True)),
                ('completed', models.BooleanField(default=False))
            ],
        ),
    ]