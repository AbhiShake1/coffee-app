# Generated by Django 4.0.4 on 2022-04-30 13:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_orderhistory_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderhistory',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 30, 13, 32, 21, 730850, tzinfo=utc)),
        ),
    ]
