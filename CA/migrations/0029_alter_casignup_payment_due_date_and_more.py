# Generated by Django 4.0.1 on 2022-03-03 09:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CA', '0028_auto_20220302_0405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casignup',
            name='payment_due_date',
            field=models.DateField(default=datetime.datetime(2022, 3, 18, 9, 8, 43, 135167)),
        ),
        migrations.AlterField(
            model_name='prsignup',
            name='payment_due_date',
            field=models.DateField(default=datetime.datetime(2022, 3, 18, 9, 8, 43, 135476)),
        ),
    ]
