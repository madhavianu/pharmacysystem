from django.db import models  # Ensure this import is included
from django.utils import timezone
from datetime import timedelta

class Medicine(models.Model):
    name = models.CharField(max_length=100)  # Field for medicine name
    mrp = models.DecimalField(max_digits=10, decimal_places=2)  # Field for MRP
    mfg_date = models.DateField(default=timezone.now)  # Current date by default
    expiry_date = models.DateField(default=timezone.now() + timedelta(days=365))  # 1 year from now by default
    quantity = models.PositiveIntegerField(default=0)  # Default quantity as 0

    def __str__(self):
        return self.name  # Display medicine name as string representation
