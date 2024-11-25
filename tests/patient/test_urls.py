from django.urls import reverse, resolve
from django.test import SimpleTestCase
from patient.views import patient_list, patient_add, patient_edit, patient_delete

class PatientUrlsTest(SimpleTestCase):

    def test_patient_list_url_is_resolved(self):
        url = reverse('patient_list')
        self.assertEqual(resolve(url).func, patient_list)

    def test_patient_add_url_is_resolved(self):
        url = reverse('patient_add')
        self.assertEqual(resolve(url).func, patient_add)

    def test_patient_edit_url_is_resolved(self):
        url = reverse('patient_edit', args=[1])  # Assuming an ID of 1 for testing
        self.assertEqual(resolve(url).func, patient_edit)

    def test_patient_delete_url_is_resolved(self):
        url = reverse('patient_delete', args=[1])  # Assuming an ID of 1 for testing
        self.assertEqual(resolve(url).func, patient_delete)