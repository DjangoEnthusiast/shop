# Generated by Django 5.1.1 on 2024-10-16 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shrihari', '0015_savedcard'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliverydetails',
            name='customer_city',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='deliverydetails',
            name='customer_state',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
