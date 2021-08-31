# Generated by Django 2.2.10 on 2021-07-01 04:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20210701_0346'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='Invoice_reference',
            field=models.CharField(blank=True, max_length=500, verbose_name='Invoice Reference Number'),
        ),
        migrations.AlterField(
            model_name='accessrequest',
            name='Request_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 1, 4, 34, 49, 522429), null=True, verbose_name='Date of Request'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='Invoice_Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 1, 4, 34, 49, 521280), null=True, verbose_name='Date of invoice'),
        ),
    ]
