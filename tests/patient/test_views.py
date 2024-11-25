from django.test import TestCase
from django.urls import reverse
from patient.models import Patient
from patient.forms import PatientForm

class PatientViewsTest(TestCase):

    def setUp(self):
        """Create a sample patient for testing."""
        self.patient = Patient.objects.create(
            name='John Doe',
            age=30,
            sex='Male',
            problem='Flu',
            nic='123456789012'
        )

    def test_patient_list_view(self):
        """Test that the patient list view returns a 200 response and displays patients."""
        response = self.client.get(reverse('patient_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'patient_list.html')
        self.assertContains(response, 'John Doe')

    def test_patient_add_view(self):
        """Test that the patient add view works and adds a patient."""
        response = self.client.post(reverse('patient_add'), {
            'name': 'Jane Doe',
            'age': 28,
            'sex': 'Female',
            'problem': 'Cough',
            'nic': '123456789013'
        })
        self.assertEqual(response.status_code, 302)  # Redirects after successful creation
        self.assertTrue(Patient.objects.filter(name='Jane Doe').exists())

    def test_patient_edit_view(self):
        """Test that the patient edit view works and updates a patient."""
        response = self.client.post(reverse('patient_edit', args=[self.patient.id]), {
            'name': 'John Smith',
            'age': 31,
            'sex': 'Male',
            'problem': 'Flu',
            'nic': '123456789012'
        })


        self.assertEqual(response.status_code, 302)  # Redirects after successful update
        self.patient.refresh_from_db()
        self.assertEqual(self.patient.name, 'John Smith')

    def test_patient_delete_view(self):
        """Test that the patient delete view works and deletes a patient."""
        response = self.client.post(reverse('patient_delete', args=[self.patient.id]))
        self.assertEqual(response.status_code, 302)  # Redirects after successful deletion
        self.assertFalse(Patient.objects.filter(pk=self.patient.pk).exists())

    def test_patient_add_view_invalid(self):
        """Test that the patient add view handles invalid data."""
        response = self.client.post(reverse('patient_add'), {
            'name': '',  # Invalid name
            'age': 28,
            'sex': 'Female',
            'problem': 'Cough',
            'nic': '123456789013'
        })
        self.assertEqual(response.status_code, 200)  # Should return to the form
        self.assertFormError(response, 'form', 'name', 'This field is required.')