from django.test import TestCase
from doacao.forms import AgendamentoForm
from pages.models import Produto
from recebimento.forms import EntradaAgendadaForm
from users.models import User

class DoacaoAgendadaFormTestCase(TestCase):

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


class DoacaoDiretaRecebidaFormTestCase(TestCase):

  def test_id_field_not_present(self):
    # model form excluded field
    form = EntradaAgendadaForm()
    self.assertFalse(form.fields.get('id'))

  def test_all_required_form_fields(self):
    fields_form = {
      'produto': None, 
      'quantidade': None, 
      'dataRecebimento': None, 
      'dataValidade': None
    }
    form = EntradaAgendadaForm(fields_form)
    form.is_valid()
    for key in fields_form:
      self.assertIn(key, form.errors)


class DoacaoAgendadaRecebidaFormTestCase(TestCase):

  fixtures = ['data.json']  # insere dados no banco de dados de testes

  def setUp(self):
    self.__set_initial_form()

  def test_id_field_not_present(self):
    # model form excluded field
    form = EntradaAgendadaForm(initial=self.form_initial)
    self.assertFalse(form.fields.get('id'))

  def test_all_required_form_fields(self):
    fields_form = {'dataRecebimento': None, 'dataValidade': None}
    form = EntradaAgendadaForm(fields_form, initial=self.form_initial)
    form.is_valid()
    self.assertIn('dataRecebimento', form.errors)
    self.assertIn('dataValidade', form.errors)

  def __set_initial_form(self):
    produto = Produto.objects.get(pk=1)
    doador = User.objects.get(pk=102)
    self.form_initial = {'produto': produto, 'doador': doador}
