# Generated by Django 3.0.8 on 2020-07-04 17:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200704_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 4, 17, 24, 57, 933956, tzinfo=utc)),
        ),
    ]
