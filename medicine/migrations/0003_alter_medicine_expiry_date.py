# Generated by Django 5.1.3 on 2024-11-23 13:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0002_rename_price_medicine_mrp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='expiry_date',
            field=models.DateField(default=datetime.datetime(2025, 11, 23, 13, 16, 14, 735604, tzinfo=datetime.timezone.utc)),
        ),
    ]
