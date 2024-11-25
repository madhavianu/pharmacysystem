from django.urls import reverse, resolve
from django.test import SimpleTestCase
from medicine.views import medi_list, medi_add, medi_edit, medi_delete

class UrlsTest(SimpleTestCase):

    def test_medi_list_url_resolves(self):
        url = reverse('medi_list')
        self.assertEqual(resolve(url).func, medi_list)

    def test_medi_add_url_resolves(self):
        url = reverse('medi_add')
        self.assertEqual(resolve(url).func, medi_add)

    def test_medi_edit_url_resolves(self):
        url = reverse('medi_edit', args=[1])  # Assuming a valid primary key
        self.assertEqual(resolve(url).func, medi_edit)

    def test_medi_delete_url_resolves(self):
        url = reverse('medi_delete', args=[1])  # Assuming a valid primary key
        self.assertEqual(resolve(url).func, medi_delete)