# Generated by Django 3.0.6 on 2020-05-16 05:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20200516_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='report_date',
            field=models.DateField(default=datetime.datetime(2020, 5, 16, 5, 8, 34, 172457, tzinfo=utc)),
        ),
    ]
