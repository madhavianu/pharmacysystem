from django import forms
from .models import Medicine

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['name', 'mrp', 'mfg_date', 'expiry_date', 'quantity']
