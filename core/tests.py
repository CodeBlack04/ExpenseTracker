from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class CoreViewTest(TestCase):
    def test_signup_view(self):
        response = self.client.get(reverse('core:signup'))

        self.assertEqual(response.status_code, 200)

        data = {
            'username': 'tamim1517',
            'email': 'tauhidur.rahman1517@gmail.com',
            'password1': 'abcdABCD1234',
            'password2': 'abcdABCD1234'
        }

        post_response = self.client.post(reverse('core:signup'), data)
        self.assertEqual(post_response.status_code, 302)
