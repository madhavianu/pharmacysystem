# Generated by Django 5.1.3 on 2024-11-24 21:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0016_alter_medicine_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='expiry_date',
            field=models.DateField(default=datetime.datetime(2025, 11, 24, 21, 48, 30, 969268, tzinfo=datetime.timezone.utc)),
        ),
    ]
