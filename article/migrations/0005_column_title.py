# Generated by Django 3.0.6 on 2020-05-22 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20200522_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='column',
            name='title',
            field=models.CharField(default='', max_length=64),
        ),
    ]
