# Generated by Django 3.0.5 on 2020-05-18 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Temp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('filename', models.CharField(max_length=100)),
                ('img', models.CharField(max_length=100)),
            ],
        ),
    ]
