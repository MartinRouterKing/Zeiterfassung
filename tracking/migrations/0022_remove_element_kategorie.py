# Generated by Django 2.0.1 on 2019-01-17 00:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0021_auto_20190107_0000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='element',
            name='kategorie',
        ),
    ]
