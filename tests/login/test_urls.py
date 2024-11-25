from django.urls import reverse, resolve
from django.test import SimpleTestCase
from login.views import admin_login, admin_dashboard, admin_logout

class URLTests(SimpleTestCase):

    def test_admin_login_url_resolves(self):
        url = reverse('admin_login')
        self.assertEqual(resolve(url).func, admin_login)

    def test_admin_dashboard_url_resolves(self):
        url = reverse('admin_dashboard')
        self.assertEqual(resolve(url).func, admin_dashboard)

    def test_admin_logout_url_resolves(self):
        url = reverse('admin_logout')
        self.assertEqual(resolve(url).func, admin_logout)