# Generated by Django 2.1.5 on 2019-05-28 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friendship', '0003_block_unique_together'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='block',
            options={'verbose_name': 'Blocked Relationship', 'verbose_name_plural': 'Blocked Relationships'},
        ),
    ]
