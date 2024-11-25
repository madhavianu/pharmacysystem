from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from payment.models import Transaction
from medicine.models import Medicine

User  = get_user_model()

class TransactionListViewTest(TestCase):

    def setUp(self):
        # Create an admin user
        self.admin_user = User.objects.create_superuser(
            username='admin',
            password='adminpassword',
            email='admin@example.com'
        )
        # Create a regular user
        self.regular_user = User.objects.create_user(
            username='user',
            password='userpassword'
        )
        # Create a medicine instance for testing
        self.medicine = Medicine.objects.create(name='Aspirin', quantity=10, mrp=5.0)
        # Create a transaction for testing
        self.transaction = Transaction.objects.create(
            medicine_name=self.medicine.name,
            quantity=2,
            amount=10.0,
            payment_method='Credit Card'
        )

    def test_transaction_list_access_for_admin(self):
        self.client.login(username='admin', password='adminpassword')
        response = self.client.get(reverse('transaction_list'))
        self.assertEqual(response, msg="Cannot Access")
        self.assertTemplateUsed(response, 'transaction_list.html')
        self.assertContains(response, 'Aspirin')  # Check if the transaction appears in the list
        self.assertContains(response, '2')  # Check if the quantity appears in the list
        self.assertContains(response, '10.0')  # Check if the amount appears in the list

    def test_transaction_list_access_for_non_admin(self):
        self.client.login(username='user', password='userpassword')
        response = self.client.get(reverse('transaction_list'))
        self.assertEqual(response, msg="Cannot Access" )  # Forbidden access for non-admin

    