# Generated by Django 3.0.6 on 2020-05-26 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0010_auto_20200526_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articletype',
            name='title',
            field=models.CharField(max_length=256),
        ),
    ]