from django import forms
from django.forms.fields import DateField

from pages.models import Produto, DoacaoRecebida
from users.models import User

class EntradaAgendadaForm(forms.ModelForm):

    class Meta:
        model = DoacaoRecebida
        fields = ('doador', 'produto', 'quantidade', 'dataRecebimento', 'dataValidade', )


    def __init__(self, *args, **kwargs):

        super(EntradaAgendadaForm, self).__init__(*args, **kwargs)

        self.fields['dataValidade'].widget.attrs['placeholder'] = '00/00/0000'
        self.fields['dataRecebimento'].widget.attrs['placeholder'] = '00/00/0000'
        
        initial = kwargs.get('initial')
        if initial is None:
            self.fields['doador'].queryset = User.objects.filter(administrador=False)
            self.fields['produto'].queryset = Produto.objects.filter(aceitaDoacao=True)
            self.fields['produto'].widget.attrs['autofocus'] = 'autofocus'
            return

        produto = initial.get('produto')
        doador = initial.get('doador')

        self.fields['produto'].queryset = Produto.objects.filter(id=produto.id)
        self.fields['doador'].queryset = User.objects.filter(id=doador.id)
        self.fields['produto'].empty_label = None
        self.fields['doador'].empty_label = None

        # Produto, quantidade e doador não pode ser mudado, vem do agendamento
        self.fields['dataValidade'].widget.attrs['autofocus'] = 'autofocus'
        self.fields['quantidade'].widget.attrs['readonly'] = 'readonly'
        self.fields['produto'].widget.attrs['readonly'] = 'readonly'
        self.fields['doador'].widget.attrs['readonly'] = 'readonly'
