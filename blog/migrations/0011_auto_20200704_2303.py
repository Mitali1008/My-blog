# Generated by Django 3.0.8 on 2020-07-04 17:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200704_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 4, 17, 33, 47, 601030, tzinfo=utc)),
        ),
    ]
