# Generated by Django 3.2.9 on 2022-01-15 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0010_auto_20220115_1819'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='fb_url',
            new_name='facebook_url',
        ),
    ]
