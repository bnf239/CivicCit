# Generated by Django 3.2.11 on 2022-04-24 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduling', '0005_rename_user_event_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='user_id',
            new_name='user',
        ),
    ]
