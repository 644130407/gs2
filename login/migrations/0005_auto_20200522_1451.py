# Generated by Django 3.0.6 on 2020-05-22 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20200520_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='thumb',
            field=models.CharField(default='', max_length=100),
        ),
    ]
