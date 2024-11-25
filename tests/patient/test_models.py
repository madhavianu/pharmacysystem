from django.test import TestCase
from django.core.exceptions import ValidationError  
from patient.models import Patient

class PatientModelTest(TestCase):

    def test_patient_creation(self):
        """Test that a Patient instance is created correctly."""
        patient = Patient.objects.create(
            name='John Doe',
            age=25,
            sex='Male',
            problem='Flu',
            nic='123456789012'
        )
        self.assertEqual(patient.name, 'John Doe')
        self.assertEqual(patient.age, 25)
        self.assertEqual(patient.sex, 'Male')
        self.assertEqual(patient.problem, 'Flu')
        self.assertEqual(patient.nic, '123456789012')

    def test_patient_str_method(self):
        """Test the string representation of the Patient model."""
        patient = Patient.objects.create(
            name='John Doe',
            age=25,
            sex='Male',
            problem='Flu',
            nic='123456789012'
        )
        self.assertEqual(str(patient), 'John Doe')

    def test_patient_age_validation(self):
        """Test that the age field is validated correctly."""
        with self.assertRaises(ValidationError):
            patient = Patient(
                name='John Doe',
                age=17,
                sex='Male',
                problem='Flu',
                nic='123456789012'
            )
            patient.full_clean()  

    def test_patient_nic_uniqueness(self):
        """Test that the nic field is unique."""
        Patient.objects.create(
            name='John Doe',
            age=25,
            sex='Male',
            problem='Flu',
            nic='123456789012'
        )
        with self.assertRaises(Exception):
            Patient.objects.create(
                name='Jane Doe',
                age=25,
                sex='Female',
                problem='Headache',
                nic='123456789012'
            )  # Raise an exception due to duplicate nic

    def test_patient_sex_choices(self):
        """Test that the sex field only accepts valid choices."""
        with self.assertRaises(ValidationError):
            patient = Patient(
                name='John Doe',
                age=25,
                sex='Other',  
                problem='Flu',
                nic='123456789012'
            )
            patient.full_clean()  # Raise a validation error