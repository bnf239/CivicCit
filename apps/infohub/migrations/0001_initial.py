# Generated by Django 3.2.11 on 2022-04-11 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InfoHubUserInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=1000)),
                ('url_links', models.CharField(max_length=1000)),
            ],
        ),
    ]
