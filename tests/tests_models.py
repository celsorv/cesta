from django.test import TestCase
from pages.models import UnidadeOrganizacao

class ModelsTestCase(TestCase):

  def setUp(self):
    UnidadeOrganizacao.objects.create(
      nome='Igreja Teste',
      metaQtdeCestas=99,
      diasEsperaAgendadas=30,
    )      

  def test_retorno_str(self):
    u1 = UnidadeOrganizacao.objects.get(nome="Igreja Teste")
    self.assertEqual(u1.__str__(), 'Igreja Teste')

  