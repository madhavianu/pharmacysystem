from django.test import TestCase
from medicine.models import Medicine
from datetime import timedelta
from django.utils import timezone

class MedicineModelTest(TestCase):
    def setUp(self):
        self.medicine = Medicine(
            name='Test Medicine',
            mrp=100.00,
            mfg_date='2023-01-01',  
            expiry_date='2024-01-01', 
            quantity=10
        )

    def test_medicine_name(self):
        self.assertEqual(self.medicine.name, 'Test Medicine')

    def test_medicine_mrp(self):
        self.assertEqual(self.medicine.mrp, 100.00)

    def test_medicine_mfg_date(self):
        self.assertEqual(self.medicine.mfg_date, '2023-01-01')

    def test_medicine_expiry_date(self):
        self.assertEqual(self.medicine.expiry_date, '2024-01-01')

    def test_medicine_quantity(self):
        self.assertEqual(self.medicine.quantity, 10)

    def test_medicine_string_representation(self):
        self.assertEqual(str(self.medicine), 'Test Medicine')

    