# Generated by Django 2.0.1 on 2018-11-29 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0012_elementtokat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='obj',
            field=models.TextField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='element',
            name='wie',
            field=models.TextField(default=None, max_length=100),
        ),
    ]
