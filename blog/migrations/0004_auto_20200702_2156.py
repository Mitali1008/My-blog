# Generated by Django 3.0.2 on 2020-07-02 16:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200702_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 2, 16, 26, 53, 72587, tzinfo=utc)),
        ),
    ]
