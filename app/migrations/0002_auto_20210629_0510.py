# Generated by Django 2.2.10 on 2021-06-29 05:10

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DefinedTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tag_Title', models.CharField(blank=True, max_length=20, verbose_name='Tag Title')),
                ('Tag_description', models.TextField(blank=True, verbose_name='Tag Description')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Invoice_Title', models.CharField(max_length=200, verbose_name='Invoice Title/Name')),
                ('Invoice_ContactInfo', models.CharField(blank=True, max_length=200, verbose_name='Invoice Contact Info')),
                ('Invoice_ID', models.CharField(default=' ', max_length=9, verbose_name='Invoice ID')),
                ('Invoice_Date', models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 29, 5, 10, 34, 320094), null=True, verbose_name='Date of invoice')),
                ('Invoice_Total_Amount', models.IntegerField(blank=True, default=0, verbose_name='Invoicne Total Amount')),
                ('Invoice_SubTotal_Amount', models.IntegerField(blank=True, default=0, verbose_name='Invoicne Sub Total Amount')),
                ('Invoice_member_ID', models.CharField(blank=True, max_length=20, verbose_name='Member ID')),
                ('Invoice_gst_number', models.CharField(blank=True, max_length=20, verbose_name='Invoice GST Number')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_description', models.TextField(blank=True)),
                ('Product_image', models.ImageField(blank=True, default='product_images/default_product.png', upload_to='product_images')),
                ('Product_name', models.CharField(max_length=200, verbose_name='Product Name')),
                ('Product_ID', models.CharField(default='AB1000', max_length=6, verbose_name='Product ID')),
                ('Product_mrp', models.IntegerField(default=0, verbose_name='Product MRP')),
                ('Product_sprice', models.IntegerField(blank=True, default=0, verbose_name='Product Substitute Price')),
                ('Product_sprice_tag', models.CharField(blank=True, default='Member', max_length=200, verbose_name='Product Substitute Price tag (Make sure to have commong Product tag)')),
                ('Product_gst_per', models.IntegerField(blank=True, default=0, verbose_name='Product GST percentage:')),
            ],
        ),
        migrations.AlterField(
            model_name='inventory',
            name='Inventory_name',
            field=models.CharField(blank=True, max_length=200, verbose_name='Inventory Name'),
        ),
        migrations.CreateModel(
            name='TagsTotal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Defined_Tags', models.CharField(blank=True, max_length=20, verbose_name='Tag Title')),
                ('Tag_total', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=13, verbose_name='Tag Total')),
                ('Tag_Invoice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Invoice')),
            ],
        ),
        migrations.CreateModel(
            name='SalesUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SalesUser_ID', models.CharField(default='ABCDE12345', max_length=10, unique=True, verbose_name='Sales User ID')),
                ('Invoice_GST_no', models.CharField(blank=True, default=' ', max_length=20, verbose_name='GST Number')),
                ('Sales_User_image', models.ImageField(blank=True, default='sales_user_images/default_sales_user.png', upload_to='sales_user_images')),
                ('Inventory_access', models.BooleanField(default=False)),
                ('SalesUser_Inventory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.Inventory')),
                ('Sales_User', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tag_value', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=13, verbose_name='Tag Value')),
                ('Defined_Tags', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.DefinedTags')),
                ('Tag_Item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='Product_inventory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Inventory'),
        ),
        migrations.CreateModel(
            name='ItemStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item_Count', models.IntegerField(blank=True, default=0, verbose_name='Quantity')),
                ('Item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Product')),
                ('Stock_User', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.SalesUser')),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Member', models.BooleanField(default=False)),
                ('Item_Quantity', models.IntegerField(blank=True, default=0, verbose_name='Quantity')),
                ('Item_price', models.IntegerField(blank=True, default=0, verbose_name='Price')),
                ('Item_ID', models.CharField(blank=True, max_length=6, verbose_name='Item ID')),
                ('Item_name', models.CharField(blank=True, max_length=200, verbose_name='Item Name')),
                ('Item_gst', models.IntegerField(blank=True, default=0, verbose_name='Item GST')),
                ('Item_Invoice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Invoice')),
            ],
        ),
        migrations.AddField(
            model_name='invoice',
            name='Invoice_Inventory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.Inventory'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='Invoice_User',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.SalesUser'),
        ),
        migrations.AddField(
            model_name='definedtags',
            name='Tag_inventory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Inventory'),
        ),
        migrations.CreateModel(
            name='AccessRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Request_date', models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 29, 5, 10, 34, 321203), null=True, verbose_name='Date of Request')),
                ('Request_ID', models.CharField(blank=True, max_length=20, verbose_name='Request ID')),
                ('Request_from', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.SalesUser')),
                ('Requested_Inventory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Inventory')),
            ],
        ),
    ]