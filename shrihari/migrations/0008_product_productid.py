# Generated by Django 4.2.14 on 2024-09-12 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shrihari', '0007_remove_category_covers_remove_category_earphone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='productid',
            field=models.PositiveIntegerField(editable=False, null=True, unique=True),
        ),
    ]
