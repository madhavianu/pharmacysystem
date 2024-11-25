from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.cache import cache

User  = get_user_model()

class AdminLoginViewTest(TestCase):

    def setUp(self):
        self.username = 'admin'
        self.password = 'admin123'
        self.user = User.objects.create_superuser(username=self.username, password=self.password)

    def test_admin_login_success(self):
        response = self.client.post(reverse('admin_login'), {
            'username': self.username,
            'password': self.password
        })
        self.assertRedirects(response, reverse('admin_dashboard'))

    def test_admin_login_invalid_credentials(self):
        response = self.client.post(reverse('admin_login'), {
            'username': self.username,
            'password': 'wrongpassword'
        })
        self.assertContains(response, 'Invalid username or password')

    def test_admin_login_block_after_three_attempts(self):
        for _ in range(3):
            self.client.post(reverse('admin_login'), {
                'username': self.username,
                'password': 'wrongpassword'
            })
        response = self.client.post(reverse('admin_login'), {
            'username': self.username,
            'password': 'wrongpassword'
        })
        self.assertContains(response, 'Your account is blocked due to too many failed login attempts.')

    def test_password_validation(self):
        response = self.client.post(reverse('admin_login'), {
            'username': self.username,
            'password': 'short'
        })
        self.assertContains(response, 'Password must be at least 6 characters long and include letters and numbers.')

    def test_successful_login_resets_attempts(self):
        for _ in range(3):
            self.client.post(reverse('admin_login'), {
                'username': self.username,
                'password': 'wrongpassword'
            })
        # Successful login
        self.client.post(reverse('admin_login'), {
            'username': self.username,
            'password': self.password
        })
        # Attempt to login again with wrong password
        response = self.client.post(reverse('admin_login'), {
            'username': self.username,
            'password': 'wrongpassword'
        })
        self.assertNotContains(response, 'Your account is blocked due to too many failed login attempts.')

class AdminDashboardViewTest(TestCase):

    def setUp(self):
        self.username = 'admin'
        self.password = 'admin123'
        self.user = User.objects.create_superuser(username=self.username, password=self.password)

    def test_admin_dashboard_access(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('admin_dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home_page.html')

    def test_admin_dashboard_access_without_login(self):
        response = self.client.get(reverse('admin_dashboard'))
        self.assertRedirects(response, f"{reverse('admin_login')}?next={reverse('admin_dashboard')}")