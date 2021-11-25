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
