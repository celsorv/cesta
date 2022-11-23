from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from braces.views import GroupRequiredMixin

from .forms import FamiliaAtendidaForm, FamiliaQuestionarioForm, UnidadeOrganizacaoForm, GrupoProdutoForm, ProdutoForm
from pages.models import FamiliaAtendida, FamiliaQuestionario, UnidadeOrganizacao, GrupoProduto, Produto

class UnidadeOrganizacaoEdit(GroupRequiredMixin, LoginRequiredMixin, UpdateView):

    model = UnidadeOrganizacao
    form_class = UnidadeOrganizacaoForm
    template_name = 'cadastros/unidade_org/form.html'
    success_url = reverse_lazy('pages:home')
    group_required = 'admin_users'
    redirect_field_name = '/'

class FamiliaAtendidaList(GroupRequiredMixin, LoginRequiredMixin, ListView):

    model = FamiliaAtendida
    paginate_by = 10
    context_object_name = 'db'
    template_name = 'cadastros/familia_atendida/list.html'
    group_required = 'admin_users'
    redirect_field_name = '/'

    def get_queryset(self):

        search = self.request.GET.get('search')

        queryset = FamiliaAtendida.objects.order_by('nome')

        if search:
            queryset = queryset.filter(nome__istartswith=search)

        return queryset

class FamiliaAtendidaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):

    model = FamiliaAtendida
    form_class = FamiliaAtendidaForm
    template_name = 'cadastros/familia_atendida/form.html'
    success_url = reverse_lazy('cadastros:familia_atendida_list')
    group_required = 'admin_users'
    redirect_field_name = '/'

class FamiliaAtendidaEdit(GroupRequiredMixin, LoginRequiredMixin, UpdateView):

    model = FamiliaAtendida
    form_class = FamiliaAtendidaForm
    template_name = 'cadastros/familia_atendida/form.html'
    success_url = reverse_lazy('cadastros:familia_atendida_list')
    group_required = 'admin_users'
    redirect_field_name = '/'

class FamiliaAtendidaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):

    model = FamiliaAtendida
    template_name = 'cadastros/familia_atendida/confirm_delete.html'
    success_url = reverse_lazy('cadastros:familia_atendida_list')
    group_required = 'admin_users'
    redirect_field_name = '/'

class FamiliaAtendidaQuestionario(GroupRequiredMixin, LoginRequiredMixin, UpdateView):

    model = FamiliaQuestionario
    form_class = FamiliaQuestionarioForm
    template_name = 'cadastros/familia_atendida/questionario.html'
    success_url = reverse_lazy('cadastros:familia_atendida_list')
    context_object_name = 'db'
    group_required = 'admin_users'
    redirect_field_name = '/'

    def form_valid(self, form):
        form.instance.respondido = True
        return super().form_valid(form)

class GrupoProdutoList(GroupRequiredMixin, LoginRequiredMixin, ListView):

    model = GrupoProduto
    paginate_by = 10
    context_object_name = 'db'
    template_name = 'cadastros/grupo_produto/list.html'
    group_required = 'admin_users'
    redirect_field_name = '/'

    def get_queryset(self):

        search = self.request.GET.get('search')

        queryset = GrupoProduto.objects.order_by('descricao')

        if search:
            queryset = queryset.filter(descricao__istartswith=search)

        return queryset

class GrupoProdutoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):

    model = GrupoProduto
    form_class = GrupoProdutoForm
    template_name = 'cadastros/grupo_produto/form.html'
    success_url = reverse_lazy('cadastros:grupo_produto_list')
    group_required = 'admin_users'
    redirect_field_name = '/'

class GrupoProdutoEdit(GroupRequiredMixin, LoginRequiredMixin, UpdateView):

    model = GrupoProduto
    form_class = GrupoProdutoForm
    template_name = 'cadastros/grupo_produto/form.html'
    success_url = reverse_lazy('cadastros:grupo_produto_list')
    group_required = 'admin_users'
    redirect_field_name = '/'

class GrupoProdutoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):

    model = GrupoProduto
    template_name = 'cadastros/grupo_produto/confirm_delete.html'
    success_url = reverse_lazy('cadastros:grupo_produto_list')
    group_required = 'admin_users'
    redirect_field_name = '/'

class ProdutoList(GroupRequiredMixin, LoginRequiredMixin, ListView):

    model = Produto
    paginate_by = 10
    context_object_name = 'db'
    template_name = 'cadastros/produto/list.html'
    group_required = 'admin_users'
    redirect_field_name = '/'


    def get_queryset(self):

        search = self.request.GET.get('search')

        queryset = Produto.objects.order_by('descricao')

        if search:
            queryset = queryset.filter(descricao__istartswith=search)

        return queryset

class ProdutoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):

    model = Produto
    form_class = ProdutoForm
    template_name = 'cadastros/produto/form.html'
    success_url = reverse_lazy('cadastros:produto_list')
    group_required = 'admin_users'
    redirect_field_name = '/'

class ProdutoEdit(GroupRequiredMixin, LoginRequiredMixin, UpdateView):

    model = Produto
    form_class = ProdutoForm
    template_name = 'cadastros/produto/form.html'
    success_url = reverse_lazy('cadastros:produto_list')
    group_required = 'admin_users'
    redirect_field_name = '/'

class ProdutoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):

    model = Produto
    template_name = 'cadastros/produto/confirm_delete.html'
    success_url = reverse_lazy('cadastros:produto_list')
    group_required = 'admin_users'
    redirect_field_name = '/'
