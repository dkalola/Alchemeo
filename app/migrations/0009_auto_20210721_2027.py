# Generated by Django 2.2.10 on 2021-07-21 14:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20210707_0723'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesuser',
            name='Sales_User_Terms_condition',
            field=models.TextField(blank=True, verbose_name='Terms and Condition'),
        ),
        migrations.AddField(
            model_name='salesuser',
            name='Sales_User_bnk_accnt_no',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Bank Account Number'),
        ),
        migrations.AddField(
            model_name='salesuser',
            name='Sales_User_bnk_code',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Bank Code'),
        ),
        migrations.AddField(
            model_name='salesuser',
            name='Sales_User_bnk_name',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Bank Name'),
        ),
        migrations.AddField(
            model_name='salesuser',
            name='Sales_User_info',
            field=models.TextField(blank=True, verbose_name='Information'),
        ),
        migrations.AlterField(
            model_name='accessrequest',
            name='Request_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 21, 20, 27, 23, 668286), null=True, verbose_name='Date of Request'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='Invoice_Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 21, 20, 27, 23, 667680), null=True, verbose_name='Date of invoice'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='Invoice_SubTotal_Amount',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20, verbose_name='Invoicne Sub Total Amount'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='Invoice_Total_Amount',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20, verbose_name='Invoicne Total Amount'),
        ),
    ]
