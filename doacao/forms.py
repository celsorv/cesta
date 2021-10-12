from django import forms

from pages.models import Produto, DoacaoAgendada

class AgendamentoForm(forms.ModelForm):

    class Meta:
        model = DoacaoAgendada
        fields = ('produto', 'quantidade', )


    def __init__(self, *args, **kwargs):

        super(AgendamentoForm, self).__init__(*args, **kwargs)
        
        self.fields['quantidade'].widget.attrs['readonly'] = 'readonly'
        
        initial = kwargs.get('initial')
        grupoProduto = initial.get('grupoProduto')
        
        self.fields['produto'].queryset = Produto.objects.filter(
            grupoProduto=grupoProduto,
            aceitaDoacao=True
        )
