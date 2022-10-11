from django import forms

from pages.models import FamiliaAtendida, UnidadeOrganizacao, GrupoProduto, Produto

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
        self.fields['qtdeCestas'].widget.attrs['aria-label'] = 'Informe a quantidade de cestas que a família recebe'
        self.fields['logradouro'].widget.attrs['aria-label'] = 'Informe o logradouro e número do endereço'
        self.fields['complemento'].widget.attrs['aria-label'] = 'Informe o completo do endereço'
        self.fields['bairro'].widget.attrs['aria-label'] = 'Informe o bairro do endereço'
        self.fields['telefone'].widget.attrs['aria-label'] = 'Informe os telefones de contato'
        self.fields['observacoes'].widget.attrs['aria-label'] = 'Informe observações importantes'


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
            'tipo_unitario',
            'qtdeNaEmbalagem',
            'aceitaDoacao', 
        )

    def __init__(self, *args, **kwargs):
        super(ProdutoForm, self).__init__(*args, **kwargs)
        self.fields['descricao'].widget.attrs['autofocus'] = 'autofocus'
        self.fields['descricao'].widget.attrs['aria-label'] = 'Informe a descrição do produto'
        self.fields['tipo_unitario'].widget.attrs['aria-label'] = 'Informe o tipo unitario'
        self.fields['grupoProduto'].widget.attrs['aria-label'] = 'Selecione o grupo do produto'
        self.fields['qtdeNaEmbalagem'].widget.attrs['aria-label'] = 'Informe a quantidade na embalagem'
        self.fields['aceitaDoacao'].widget.attrs['aria-label'] = 'Indique se este produto está sendo aceito como doação'
