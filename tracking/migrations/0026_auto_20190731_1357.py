# Generated by Django 2.0.7 on 2019-07-31 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0025_user_limitations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_limitations',
            name='limit',
            field=models.IntegerField(default=5, verbose_name='Beschränkung in Montaten'),
        ),
    ]
