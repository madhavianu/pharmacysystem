from django.test import TestCase
from medicine.forms import MedicineForm
from medicine.models import Medicine

class MedicineFormTest(TestCase):
    def test_form_valid(self):
        form_data = {
            'name': 'Test Medicine',
            'mrp': 100.00,
            'mfg_date': '2022-01-01',
            'expiry_date': '2023-01-01',
            'quantity': 10
        }
        form = MedicineForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        form_data = {
            'name': '',
            'mrp': 100.00,
            'mfg_date': '2022-01-01',
            'expiry_date': '2023-01-01',
            'quantity': 10
        }
        form = MedicineForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_form_fields(self):
        form = MedicineForm()
        print(form.fields) 
        self.assertTrue('name' in form.fields)
        self.assertTrue('mrp' in form.fields)
        self.assertTrue('mfg_date' in form.fields)
        self.assertTrue('expiry_date' in form.fields)
        self.assertTrue('quantity' in form.fields)