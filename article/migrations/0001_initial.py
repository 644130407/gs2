# Generated by Django 3.0.5 on 2020-05-19 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, unique=True)),
                ('sort', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('content', models.CharField(max_length=10240)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Users')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.ArticleType')),
            ],
        ),
    ]