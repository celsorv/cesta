from django.test import TestCase
from django.urls import reverse

class LoginTestCase(TestCase):

  def test_login_dashboard(self):
    response = self.client.get(reverse('dashboard:view'))
    self.assertRedirects(response, '/accounts/login/?redirect_to=/dashboard/')

  def test_login_doacao(self):
    response = self.client.get(reverse('doacao:list'))
    self.assertRedirects(response, '/accounts/login/?next=/doacao/')

