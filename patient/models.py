from django.db import models
from django.core.exceptions import ValidationError

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    problem = models.CharField(max_length=255)
    nic = models.CharField(max_length=12, unique=True)

    def clean(self):
        if self.age is not None and self.age < 18:
            raise ValidationError("Age must be at least 18.")
        
    def __str__(self):
        return self.name
