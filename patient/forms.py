from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'age', 'sex', 'problem', 'nic']

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age is not None and age < 18:
            raise forms.ValidationError("Age must be at least 18.")
        return age

    def clean_nic(self):
        nic = self.cleaned_data.get('nic')
        if Patient.objects.filter(nic=nic).exists():
            raise forms.ValidationError("This NIC is already in use.")
        return nic