from django.db import transaction
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from braces.views import GroupRequiredMixin

from pages.models import DoacaoAgendada, DoacaoRecebida

from .forms import EntradaAgendadaForm

from services.doacao_service import DoacaoService


class RecebimentoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    
    model = DoacaoAgendada
    context_object_name = 'db'
    paginate_by = 20
    template_name = 'recebimento/recebimento_list.html'
    group_required = 'admin_users'
    redirect_field_name = '/'

    def get_queryset(self):

        search = self.request.GET.get('search')
        field = self.request.GET.get('field')

        if search:
            if field == 'd':
                return DoacaoService.listByDoador(self, search)
            else:
                return DoacaoService.listByProduto(self, search)

        return DoacaoService.listAll()


class RecebimentoDetail(GroupRequiredMixin, LoginRequiredMixin, DetailView):

    model = DoacaoRecebida
    context_object_name = 'db'
    template_name = 'recebimento/recebimento_view.html'
    group_required = 'admin_users'
    redirect_field_name = '/'


class RecebimentoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):

    model = DoacaoRecebida
    form_class = EntradaAgendadaForm
    template_name = 'recebimento/recebimento_form.html'
    success_url = reverse_lazy('recebimento:list')
    group_required = 'admin_users'
    redirect_field_name = '/'

    doacaoAgendada = None


    def get_initial(self):

        if self.kwargs.get('pk') is None: return
        self.doacaoAgendada = DoacaoService.getById(self, self.kwargs.get('pk'))

        return {
            'doacaoAgendada': self.doacaoAgendada,
            'produto': self.doacaoAgendada.produto,
            'doador': self.doacaoAgendada.doador
        }


class RecebidosConsulta(GroupRequiredMixin, LoginRequiredMixin, ListView):
    
    model = DoacaoRecebida
    context_object_name = 'db'
    paginate_by = 20
    template_name = 'recebimento/recebimento_produto_list.html'
    group_required = 'admin_users'
    redirect_field_name = '/'

    def get_queryset(self):
        self.pk = self.kwargs.get('pk')
        return DoacaoService.listProdutoRecebimentos(self, self.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grupoProdutoDescricao'] = DoacaoService.getNomeGrupoProduto(self, self.pk)
        return context
