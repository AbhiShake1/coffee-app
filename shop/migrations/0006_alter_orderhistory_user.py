# Generated by Django 4.0.4 on 2022-04-29 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_rewardpoint_user_orderhistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderhistory',
            name='user',
            field=models.CharField(max_length=200),
        ),
    ]
