# Generated by Django 2.0.1 on 2019-01-29 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0023_auto_20190123_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='wie',
            field=models.TextField(default=None, max_length=100, null=True),
        ),
    ]
