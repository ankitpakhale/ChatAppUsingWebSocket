# Generated by Django 3.2.9 on 2022-03-02 04:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CA', '0027_auto_20220302_0405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casignup',
            name='payment_due_date',
            field=models.DateField(default=datetime.datetime(2022, 3, 17, 4, 5, 40, 836352)),
        ),
        migrations.AlterField(
            model_name='prsignup',
            name='payment_due_date',
            field=models.DateField(default=datetime.datetime(2022, 3, 17, 4, 5, 40, 836712)),
        ),
    ]
