from unittest import skip
from django.test import TestCase
from cadastros.forms import UnidadeOrganizacaoForm
from doacao.forms import AgendamentoForm
from pages.models import GrupoProduto
from users.models import User

class DoacaoAgendadaFormTestCase(TestCase):

  fixtures = ['data.json']  # insere dados no banco de dados de testes

  def setUp(self):
    self.grupoProduto = 1

  def test_id_field_not_present(self):
    # model form excluded field
    form = AgendamentoForm(initial={'grupoProduto': self.grupoProduto})
    self.assertFalse(form.fields.get('id'))

  def test_all_required_form_fields(self):
    fields_form = {'produto': None, 'quantidade': None}
    form = AgendamentoForm(fields_form, initial={'grupoProduto': self.grupoProduto})
    form.is_valid()
    self.assertIn('produto', form.errors)
    self.assertIn('quantidade', form.errors)

  def test_quantity_must_be_greater_than_zero(self):
    fields_form = {'produto': 1, 'quantidade': 0}
    form = AgendamentoForm(fields_form, initial={'grupoProduto': self.grupoProduto})
    form.is_valid()
    self.assertNotIn('produto', form.errors)
    self.assertIn('quantidade', form.errors)

  """
  def test_unidade_organizacao_form_valido(self):
    form = UnidadeOrganizacaoForm(data={
      'nome': 'Igreja Teste',
      'metaQtdeCestas': 10,
      'diasEsperaAgendadas': 5
    })
    self.assertTrue(form.is_valid())

  def test_unidade_organizacao_form_invalido(self):
    form = UnidadeOrganizacaoForm(data={})
    self.assertFalse(form.is_valid())
  """