# Generated by Django 2.1.5 on 2019-05-27 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20190527_1755'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friends',
            name='from_user',
        ),
        migrations.RemoveField(
            model_name='friends',
            name='to_user',
        ),
        migrations.RemoveField(
            model_name='user',
            name='friends',
        ),
        migrations.DeleteModel(
            name='Friends',
        ),
    ]
