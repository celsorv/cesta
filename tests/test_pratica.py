
# https://www.digitalocean.com/community/tutorials/how-to-add-unit-testing-to-your-django-project-pt

from django.test import TestCase

class ModelsTestCase(TestCase):
  
  def test_alguma_coisa(self):
    bola = 'amarela'
    self.assertEqual(bola, 'amarela')