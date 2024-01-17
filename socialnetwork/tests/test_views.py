from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import authenticate


class ViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass', email='test@gmail.com')


    def test_view_index_get(self):
        url = reverse('index')
        response = self.client.get(url) 
        self.assertEqual(response.status_code, 200)

    
    def test_login_success(self):
        url = reverse('index')
        data = {
            'email': self.user.email,
            'password': 'testpass',
            'Login': 'Log in'
        }
        response = self.client.post(url, data)
        self.assertRedirects(response, reverse('home_page'))


    def test_login_invalid(self):
        url = reverse('index')
        data = {
            'email': self.user.email,
            'password': 'testpass1',
            'Login': 'Log in'
        }
        response = self.client.post(url, data)
        self.assertFormError(response, form='form_login', field=None, errors='Invalid password')

    
    def test_view_home_page(self):
        url = reverse('home_page')
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news.html')
    

    def test_view_profile(self):
        url = reverse('profile')
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')

