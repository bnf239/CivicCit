# Generated by Django 3.2.11 on 2022-04-24 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infohub', '0004_infohubuserinformation_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='infohubuserinformation',
            old_name='user_id',
            new_name='user',
        ),
    ]
