# Generated by Django 3.2.11 on 2022-04-05 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduling', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='id',
        ),
        migrations.AlterField(
            model_name='event',
            name='event_link',
            field=models.CharField(max_length=500, primary_key=True, serialize=False),
        ),
    ]
