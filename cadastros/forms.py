from django import forms

from pages.models import UnidadeOrganizacao, GrupoProduto, Produto

class UnidadeOrganizacaoForm(forms.ModelForm):

    class Meta:
        model = UnidadeOrganizacao
        fields = (
            'metaQtdeCestas', 
            'diasEsperaAgendadas',
        )

    def __init__(self, *args, **kwargs):
        super(UnidadeOrganizacaoForm, self).__init__(*args, **kwargs)
        self.fields['metaQtdeCestas'].widget.attrs['autofocus'] = 'autofocus'
        self.fields['metaQtdeCestas'].widget.attrs['aria-label'] = 'Informe a meta em quantidade de cestas'
        self.fields['diasEsperaAgendadas'].widget.attrs['aria-label'] = 'Informe quantos dias esperar pela entrega de uma doação agendada'

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
