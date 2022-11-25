from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Layout, Fieldset, Submit
from crispy_forms.bootstrap import InlineRadios

from pages.models import FamiliaAtendida, FamiliaQuestionario, UnidadeOrganizacao, GrupoProduto, Produto

class UnidadeOrganizacaoForm(forms.ModelForm):

    class Meta:
        model = UnidadeOrganizacao
        fields = (
            'diasEsperaAgendadas',
        )

    def __init__(self, *args, **kwargs):
        super(UnidadeOrganizacaoForm, self).__init__(*args, **kwargs)
        self.fields['diasEsperaAgendadas'].widget.attrs['autofocus'] = 'autofocus'
        self.fields['diasEsperaAgendadas'].widget.attrs['aria-label'] = 'Informe quantos dias esperar pela entrega de uma doação agendada'

class FamiliaAtendidaForm(forms.ModelForm):

    class Meta:
        model = FamiliaAtendida
        fields = (
            'nome', 
            'ativo', 
            'dataDesativacao',
            'qtdeCestas',
            'logradouro',
            'complemento',
            'bairro',
            'telefone',
            'observacoes',
        )
        widgets = {
            'observacoes': forms.Textarea(),
        }

    def __init__(self, *args, **kwargs):
        super(FamiliaAtendidaForm, self).__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs['autofocus'] = 'autofocus'
        self.fields['nome'].widget.attrs['aria-label'] = 'Informe o nome da família'
        self.fields['ativo'].widget.attrs['aria-label'] = 'Indique se esta família está apta a receber cestas'
        self.fields['dataDesativacao'].widget.attrs['aria-label'] = 'Indique a data de desligamento da família no sistema'
        self.fields['qtdeCestas'].widget.attrs['aria-label'] = 'Informe a quantidade de cestas que a família recebe'
        self.fields['logradouro'].widget.attrs['aria-label'] = 'Informe o logradouro e número do endereço'
        self.fields['complemento'].widget.attrs['aria-label'] = 'Informe o completo do endereço'
        self.fields['bairro'].widget.attrs['aria-label'] = 'Informe o bairro do endereço'
        self.fields['telefone'].widget.attrs['aria-label'] = 'Informe os telefones de contato'
        self.fields['observacoes'].widget.attrs['aria-label'] = 'Informe observações importantes'

class FamiliaQuestionarioForm(forms.ModelForm):

    class Meta:
        model = FamiliaQuestionario
        exclude = ['familia', 'respondido']

    def __init__(self, *args, **kwargs):
        super(FamiliaQuestionarioForm, self).__init__(*args, **kwargs)

        choice_yes_no = [(True, 'Sim'), (False, 'Não')]
        self.fields['tipoMoradia'] = forms.ChoiceField(
            choices=FamiliaQuestionario.TIPO_MORADIA, 
            widget=forms.RadioSelect,
            label='1. Qual o tipo de moradia onde a família reside?',
        )
        self.fields['moradiaLugarViolento'] = forms.ChoiceField(
            choices=choice_yes_no, 
            widget=forms.RadioSelect,
            label='2. Você considera o lugar onde mora violento?',
        )
        self.fields['motivoLugarViolento'] = forms.ChoiceField(
            choices=FamiliaQuestionario.TIPO_VIOLENCIA, 
            widget=forms.RadioSelect,
            label='2.1. Por quê?',
        )
        self.fields['criancasFrequentamEscola'] = forms.ChoiceField(
            choices=FamiliaQuestionario.CRIANCAS_NA_ESCOLA, 
            widget=forms.RadioSelect,
            label='5. As crianças frequentam a escola regularmente?',
        )
        self.fields['temPessoasDoentes'] = forms.ChoiceField(
            choices=choice_yes_no, 
            widget=forms.RadioSelect,
            label='6. Das pessoas que residem na casa há alguma doente/ em \
                        tratamento ou com necessidades especiais?',
        )
        self.fields['rendaBrutaFamiliar'] = forms.ChoiceField(
            choices=FamiliaQuestionario.RENDA_BRUTA_FAMILIAR, 
            widget=forms.RadioSelect,
            label='11. Qual a renda bruta familiar mensal?',
        )
        self.fields['recebeAuxilioGoverno'] = forms.ChoiceField(
            choices=choice_yes_no, 
            widget=forms.RadioSelect,
            label=('12. Algum membro da família recebe algum tipo de auxílio' +
                        'ou benefício do governo, como bolsa família, ' +
                        'auxílio doença, entre outros?'
                  ),
        )
        self.fields['maiorGrauEscolaridade'] = forms.ChoiceField(
            choices=FamiliaQuestionario.GRAU_ESCOLARIDADE, 
            widget=forms.RadioSelect,
            label='13. Qual o grau de escolaridade dos adultos que residem na casa?',
        )
        self.fields['frequentaReligiao'] = forms.ChoiceField(
            choices=FamiliaQuestionario.RELIGIAO, 
            widget=forms.RadioSelect,
            label='14. Os membros da família frequentam alguma religião?',
        )


class GrupoProdutoForm(forms.ModelForm):

    class Meta:
        model = GrupoProduto
        fields = (
            'descricao', 
            'unidadeEmbalagem', 
            'qtdeNaEmbalagem',
            'unidadesNaCesta',
            'diasValidadeMinima',
            'compoeCesta', 
        )

    def __init__(self, *args, **kwargs):
        super(GrupoProdutoForm, self).__init__(*args, **kwargs)
        self.fields['descricao'].widget.attrs['autofocus'] = 'autofocus'
        self.fields['descricao'].widget.attrs['aria-label'] = 'Informe a descrição do grupo'
        self.fields['unidadeEmbalagem'].widget.attrs['aria-label'] = 'Selecione a unidade de embalagem do grupo'
        self.fields['qtdeNaEmbalagem'].widget.attrs['aria-label'] = 'Informe a quantidade na embalagem'
        self.fields['unidadesNaCesta'].widget.attrs['aria-label'] = 'Informe a quantidade que vai na cesta'
        self.fields['diasValidadeMinima'].widget.attrs['aria-label'] = 'Informe em dias a validade mínima para cesta'
        self.fields['compoeCesta'].widget.attrs['aria-label'] = 'Indique se este grupo de produtos participa da cesta'

class ProdutoForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = (
            'descricao',
            'grupoProduto',
            'qtdeNaEmbalagem',
            'aceitaDoacao', 
        )

    def __init__(self, *args, **kwargs):
        super(ProdutoForm, self).__init__(*args, **kwargs)
        self.fields['descricao'].widget.attrs['autofocus'] = 'autofocus'
        self.fields['descricao'].widget.attrs['aria-label'] = 'Informe a descrição do produto'
        self.fields['grupoProduto'].widget.attrs['aria-label'] = 'Selecione o grupo do produto'
        self.fields['qtdeNaEmbalagem'].widget.attrs['aria-label'] = 'Informe a quantidade na embalagem'
        self.fields['aceitaDoacao'].widget.attrs['aria-label'] = 'Indique se este produto está sendo aceito como doação'
