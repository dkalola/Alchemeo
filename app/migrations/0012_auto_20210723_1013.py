# Generated by Django 2.2.10 on 2021-07-23 04:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20210722_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesuser',
            name='Sales_User_include_bnkdetails',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='accessrequest',
            name='Request_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 23, 10, 13, 11, 217633), null=True, verbose_name='Date of Request'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='Invoice_Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 23, 10, 13, 11, 217005), null=True, verbose_name='Date of invoice'),
        ),
    ]
