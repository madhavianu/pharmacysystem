from django.test import TestCase
from patient.forms import PatientForm
from patient.models import Patient  

class PatientFormTest(TestCase):

    def test_valid_form(self):
        """Test that a valid form is accepted."""
        form_data = {
            'name': 'John Doe',
            'age': 25,
            'sex': 'Male',
            'problem': 'Flu',
            'nic': '123456789012'
        }
        form = PatientForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['name'], 'John Doe')
        self.assertEqual(form.cleaned_data['age'], 25)

    def test_age_validation(self):
        """Test that the form raises a validation error for age under 18."""
        form_data = {
            'name': 'Jane Doe',
            'age': 17,  # Invalid age
            'sex': 'Female',
            'problem': 'Headache',
            'nic': '123456789013'
        }
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('age', form.errors)  # Check for 'age' in errors
        self.assertEqual(form.errors['age'], ["Age must be at least 18."])  # Adjust based on your error message

    def test_empty_form(self):
        """Test that an empty form is invalid."""
        form = PatientForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)
        self.assertIn('age', form.errors)
        self.assertIn('sex', form.errors)
        self.assertIn('problem', form.errors)
        self.assertIn('nic', form.errors)

    def test_nic_uniqueness(self):
        """Test that the NIC field is unique (if applicable)."""
        # Create a patient to ensure NIC uniqueness
        Patient.objects.create(
            name='John Doe',
            age=25,
            sex='Male',
            problem='Flu',
            nic='123456789012'
        )
        form_data = {
            'name': 'Jane Doe',
            'age': 30,
            'sex': 'Female',
            'problem': 'Cough',
            'nic': '123456789012'  # Duplicate NIC
        }
        form = PatientForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('nic', form.errors)
        self.assertEqual(form.errors ['nic'], ["This NIC is already in use."]) 