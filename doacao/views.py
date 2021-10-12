from django.views.generic import ListView, UpdateView, CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from pages.models import DoacaoAgendada 
from .forms import AgendamentoForm

from services.doacao_service import DoacaoService
from services.grupo_produto_service import GrupoProdutoService


class AgendamentoList(LoginRequiredMixin, ListView):
    
    model = DoacaoAgendada
    context_object_name = 'db'
    template_name = 'doacao/doacao_list.html'

    def get_queryset(self):
        return DoacaoService.itensCestas()


class AgendamentoCreate(LoginRequiredMixin, CreateView):
    
    model = DoacaoAgendada
    form_class = AgendamentoForm
    template_name = 'doacao/doacao_form.html'
    success_url = reverse_lazy('doacao:doacao_ok')

    grupoProduto = None


    def get_initial(self):
        self.grupoProduto = GrupoProdutoService().getById(self.kwargs.get('pk'))
        success_message = self.request.user.first_name
        return {
            'grupoProduto': self.grupoProduto,
        }


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grupoProduto'] = self.grupoProduto
        return context


    def form_valid(self, form):
        form.instance.doador = self.request.user
        return super().form_valid(form)


class AgendamentoOk(LoginRequiredMixin, TemplateView):
    template_name = 'doacao/doacao_ok.html'
