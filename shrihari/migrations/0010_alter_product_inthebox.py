# Generated by Django 4.2.14 on 2024-09-13 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shrihari', '0009_remove_product_productid_product_batterycapacity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='inthebox',
            field=models.CharField(max_length=2000, null=True),
        ),
    ]
