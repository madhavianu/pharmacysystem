# Generated by Django 5.1.3 on 2024-11-24 21:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0014_alter_medicine_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='expiry_date',
            field=models.DateField(default=datetime.datetime(2025, 11, 24, 21, 38, 54, 334991, tzinfo=datetime.timezone.utc)),
        ),
    ]
