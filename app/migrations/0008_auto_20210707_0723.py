# Generated by Django 2.2.10 on 2021-07-07 07:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20210701_0434'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesuser',
            name='SalesUser_Address',
            field=models.TextField(blank=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='accessrequest',
            name='Request_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 7, 7, 23, 52, 251469), null=True, verbose_name='Date of Request'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='Invoice_Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 7, 7, 23, 52, 250598), null=True, verbose_name='Date of invoice'),
        ),
    ]
