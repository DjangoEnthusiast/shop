# Generated by Django 5.1.1 on 2024-10-15 08:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shrihari', '0014_alter_deliverydetails_order_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='savedcard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_holder_name', models.CharField(max_length=100)),
                ('card_number', models.CharField(max_length=16, validators=[django.core.validators.MaxLengthValidator(16)])),
                ('expiry_date', models.CharField(max_length=5, validators=[django.core.validators.MaxLengthValidator(5)])),
                ('cvv', models.CharField(max_length=3, validators=[django.core.validators.MaxLengthValidator(3)])),
            ],
        ),
    ]
