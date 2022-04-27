# Generated by Django 4.0.1 on 2022-01-19 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='signUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30)),
                ('email', models.EmailField(default='', max_length=254)),
                ('number', models.PositiveIntegerField(default='')),
                ('password', models.CharField(default='', max_length=15)),
                ('confirmPassword', models.CharField(default='', max_length=15)),
            ],
        ),
    ]