# Generated by Django 3.2.11 on 2022-02-01 10:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CA', '0020_auto_20220131_0415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casignup',
            name='payment_due_date',
            field=models.DateField(default=datetime.datetime(2022, 2, 16, 10, 25, 52, 427151)),
        ),
        migrations.AlterField(
            model_name='prsignup',
            name='payment_due_date',
            field=models.DateField(default=datetime.datetime(2022, 2, 16, 10, 25, 52, 427475)),
        ),
    ]