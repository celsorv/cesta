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
from pages.models import DoacaoRecebida, FamiliaAtendida, FamiliaQuestionario
from django.db.models import Sum, Q, Count, Avg
from django.db.models.functions import ExtractMonth, ExtractYear, Coalesce


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


def relatorios(request):
    return render(request, 'relatorios.html')


def cestas_doadas(request):
    dataInicial = '2022-01-01'
    dataFinal = '2023-01-01'

    queryset = (FamiliaAtendida.objects.filter(
            Q(ativo=True), #| Q(dataDesativacao__gte = dataFinal), 
            dataCadastro__gte = dataInicial and Q(dataCadastro__lt = dataFinal)
        )
        .annotate(year=ExtractYear('dataCadastro'))
        .annotate(month=ExtractMonth('dataCadastro'))
        .values('year', 'month')
        .annotate(
            total_cestas=Sum('qtdeCestas')
        )
        .order_by('year', 'month')
    )
    labels = []
    data = []

    for cesta in queryset:
        labels.append(f"{cesta['year']}-{cesta['month']}")
        data.append(cesta['total_cestas'])
    
    contexto = {
        'titulo': 'Cestas doadas em 2022',
        'labels': labels,
        'data': data,
        'chart_type': 'bar',
        'legenda': 'Cestas doadas'
    }
    return render(request, 'graficos_base.html', contexto)


def renda_familiar(request):
    queryset = (FamiliaQuestionario.objects
    .filter(Q(rendaBrutaFamiliar__isnull=False) )
    .values('rendaBrutaFamiliar')
    .annotate(
            qtd_familias=Count('familia_id')
        )
    .order_by('rendaBrutaFamiliar')
    )

    labels = []
    data = []
    labels_meaning = {
        'MENOS1': 0, 
        'EXATO1': 1, 
        'EXATO2': 2, 
        'EXATO3': 3, 
        'ACIMA3': 4, 
    }
    labels_meaning2 = [
        'Até um salário mínimo',
        'Um salário mínimo',
        'Dois salários mínimos',
        'Três salários mínimos',
        'Acima de três salários mínimos']

    for item in queryset:
        item['rendaBrutaFamiliar'] = labels_meaning[item['rendaBrutaFamiliar']]

    queryset = list(queryset)
    queryset.sort(key=lambda item: item.get("rendaBrutaFamiliar"))

    for renda in queryset:
        labels.append(labels_meaning2[renda['rendaBrutaFamiliar']])
        data.append(renda['qtd_familias'])
    
    contexto = {
        'titulo': 'Renda Familiar',
        'labels': labels,
        'data': data,
        'chart_type': 'bar',
        'legenda': 'Quantidade familias'
    }
    return render(request, 'graficos_base.html', contexto)

def analise_familias(request):
    tot_familias = FamiliaAtendida.objects.aggregate(Count('id'))['id__count']
    tot_quest_familias = FamiliaQuestionario.objects.filter(respondido=True).aggregate(Count('familia_id'))['familia_id__count']
    tot_membros = FamiliaQuestionario.objects.aggregate(tot_membros=Sum(Coalesce('pessoasNaCasa', 2)))['tot_membros']

    kids = FamiliaQuestionario.objects.aggregate(kids=Sum(Coalesce('pessoasMenores', 0)))['kids']
    kids_escola = FamiliaQuestionario.objects.filter(criancasFrequentamEscola=True).aggregate(kids_escola=Count('criancasFrequentamEscola'))['kids_escola']

    perigoso = FamiliaQuestionario.objects.filter(moradiaLugarViolento=True).aggregate(Count('familia_id'))['familia_id__count']
    trab_informal = FamiliaQuestionario.objects.aggregate(trab_informal=Coalesce(Sum('qtdeTrabalhoInformal'), 0))['trab_informal']

    gov_auxilio = FamiliaQuestionario.objects.aggregate(gov_auxilio = Count('recebeAuxilioGoverno'))['gov_auxilio']

    from django.db import connection
    cursor = connection.cursor()
    cursor.execute("select case when (maiorGrauEscolaridade) is null then 'sem_dados' else maiorGrauEscolaridade end , count(*) from pages_familiaquestionario pf group by maiorGrauEscolaridade")
    escola = dict(cursor.fetchall())

    fun_in = round(escola.get('FUN_IN', 0) / tot_familias * 100, 2)
    med_in = round(escola.get('MED_IN', 0) / tot_familias * 100, 2)
    sup_in = round(escola.get('SUP_IN', 0) / tot_familias * 100, 2)
    fun_cp = round(escola.get('FUN_CP', 0) / tot_familias * 100, 2)
    med_cp = round(escola.get('MED_CP', 0) / tot_familias * 100, 2)
    sup_cp = round(escola.get('SUP_CP', 0) / tot_familias * 100, 2)
    sem_dados = round(escola.get('sem_dados', 0) / tot_familias * 100, 2)

    contexto = {
        'tot_familias': tot_familias,
        'tot_quest_familias': tot_quest_familias,
        'tot_membros': tot_membros,
        'perigoso': round(perigoso / tot_familias * 100, 2),
        'kids': round(kids / tot_familias * 100, 2),
        'kids_escola': round(kids_escola / tot_familias *100, 2),
        'trab_informal': round(trab_informal / tot_membros * 100, 2),
        'fun_in' : fun_in,
        'med_in' : med_in,
        'sup_in' : sup_in,
        'fun_cp': fun_cp,
        'med_cp': med_cp,
        'sup_cp': sup_cp,
        'sem_dados': sem_dados,
        'gov_auxilio': round(gov_auxilio, 2),
    }
    return render(request, 'relatorio_analise_familias.html', contexto)
    