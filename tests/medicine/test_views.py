from django.test import TestCase, Client
from django.urls import reverse
from medicine.models import Medicine
from medicine.views import medi_list, medi_add, medi_edit, medi_delete

class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.medicine = Medicine.objects.create(
            name='Test Medicine',
            mrp=100.00,
            mfg_date='2022-01-01',
            expiry_date='2023-01-01',
            quantity=10
        )

    def test_medi_list_view(self):
        response = self.client.get(reverse('medi_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'medi_list.html')
        self.assertContains(response, self.medicine.name)

    def test_medi_add_view(self):
        response = self.client.get(reverse('medi_add'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'medi_add.html')

        data = {
            'name': 'New Medicine',
            'mrp': 200.00,
            'mfg_date': '2022-01-01',
            'expiry_date': '2023-01-01',
            'quantity': 20
        }
        response = self.client.post(reverse('medi_add'), data)
        self.assertEqual(response.status_code, 302)  # Redirect to medi_list

    def test_medi_edit_view(self):
        response = self.client.get(reverse('medi_edit', args=[self.medicine.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'medi_edit.html')

        data = {
            'name': 'Updated Medicine',
            'mrp': 150.00,
            'mfg_date': '2022-01-01',
            'expiry_date': '2023-01-01',
            'quantity': 30
        }
        response = self.client.post(reverse('medi_edit', args=[self.medicine.pk]), data)
        self.assertEqual(response.status_code, 302)  # Redirect to medi_list

    def test_medi_delete_view(self):
        response = self.client.get(reverse('medi_delete', args=[self.medicine.pk]))
        self.assertEqual(response.status_code, 405)  # Invalid request method

        response = self.client.post(reverse('medi_delete', args=[self.medicine.pk]))
        self.assertEqual(response.status_code, 302)  # Redirect to medi_list