from django.views.generic import TemplateView
from django.shortcuts import render, redirect

from users.models  import User

class HomePageView(TemplateView):
    template_name = 'home.html'

    def dispatch(self, request, *args, **kwargs):

        if self.request.user.is_authenticated:
            adm = User.objects.filter(pk=self.request.user.id).values('administrador')
            if adm[0].get('administrador'):
                return redirect('dashboard/')

        return super(HomePageView, self).dispatch(request, *args, **kwargs)




####
from pages.models import DoacaoRecebida
from django.db.models.aggregates import Sum


def query_doacaorecebida():
    queryset = (DoacaoRecebida.objects
    .select_related('produto')
    .values('produto__descricao')
    .annotate(total_qtd=Sum('quantidade'))
    .order_by('-total_qtd')
    )
    return queryset


def produtos_mais_doados(request):
    labels = []
    data = []

    for produtos_recebidos in query_doacaorecebida():
        labels.append(produtos_recebidos['produto__descricao'])
        data.append(produtos_recebidos['total_qtd'])

    contexto = {
        'labels': labels,
        'data': data,
        'chart_type': 'bar',
        'legenda': 'Produtos mais doados'
    }
    return render(request, 'produtos_grafico.html', contexto)
