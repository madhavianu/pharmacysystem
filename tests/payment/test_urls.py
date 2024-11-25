from django.urls import reverse
from django.test import SimpleTestCase

class PaymentUrlsTest(SimpleTestCase):

    def test_create_payment_url(self):
        url = reverse('create_payment')
        self.assertEqual(url, '/payment/createpayment/')  

    def test_transaction_list_url(self):
        url = reverse('transaction_list')
        self.assertEqual(url, '/payment/transactionlist/')  
