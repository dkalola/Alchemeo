# Generated by Django 2.2.10 on 2021-07-01 03:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210701_0342'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='Invoice_status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='accessrequest',
            name='Request_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 1, 3, 46, 27, 611478), null=True, verbose_name='Date of Request'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='Invoice_Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 1, 3, 46, 27, 610471), null=True, verbose_name='Date of invoice'),
        ),
    ]
