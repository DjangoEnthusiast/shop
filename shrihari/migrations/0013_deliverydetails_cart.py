# Generated by Django 5.1.1 on 2024-10-10 08:32

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shrihari', '0012_rename_internalstoragetorage_product_internalstorage'),
    ]

    operations = [
        migrations.CreateModel(
            name='deliverydetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=255)),
                ('customer_address', models.CharField(max_length=500)),
                ('customer_contact', models.CharField(max_length=50)),
                ('customer_pincode', models.CharField(max_length=6)),
                ('customer_email', models.CharField(max_length=225)),
                ('order_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products', models.ManyToManyField(to='shrihari.product')),
            ],
        ),
    ]
