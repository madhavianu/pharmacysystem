from django.test import TestCase
from payment.models import Medicine, Transaction
from django.core.exceptions import ValidationError

class MedicineModelTest(TestCase):

    def setUp(self):
        self.medicine = Medicine.objects.create(
            name='Aspirin',
            price=10.00,
            quantity=100
        )

    def test_medicine_creation(self):
        self.assertEqual(self.medicine.name, 'Aspirin')
        self.assertEqual(self.medicine.price, 10.00)
        self.assertEqual(self.medicine.quantity, 100)

    def test_medicine_str(self):
        self.assertEqual(str(self.medicine), 'Aspirin')

class TransactionModelTest(TestCase):

    def setUp(self):
        self.medicine = Medicine.objects.create(
            name='Aspirin',
            price=10.00,
            quantity=100
        )
        self.transaction = Transaction.objects.create(
            medicine_name=self.medicine.name,
            quantity=2,
            amount=20.00,
            payment_method='Credit Card'
        )

    def test_transaction_creation(self):
        self.assertEqual(self.transaction.medicine_name, 'Aspirin')
        self.assertEqual(self.transaction.quantity, 2)
        self.assertEqual(self.transaction.amount, 20.00)
        self.assertEqual(self.transaction.payment_method, 'Credit Card')

    def test_transaction_str(self):
        self.assertEqual(str(self.transaction), '$20.00 - Credit Card')



