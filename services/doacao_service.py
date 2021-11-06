from django.db.models import Sum, Min, F, Q, Value, IntegerField, ExpressionWrapper
from django.db.models.functions import Lower, Cast
from django.db import transaction
from datetime import datetime, timedelta

from pages.models import GrupoProduto, Produto, DoacaoAgendada, DoacaoRecebida
from .unidadeorg_service import UnidadeOrganizacaoService as orgService

class DoacaoService():

    ORG = orgService.getRecord()

    @transaction.atomic
    def fecharCestas():

        cestasCompletas = DoacaoService.__getQtdeCestasCompletas()
        if cestasCompletas is None: return

        itensCesta = GrupoProduto.objects.filter(
                compoeCesta = True
            ).annotate(
                qtNaCesta = F('qtdeNaEmbalagem') * F('unidadesNaCesta')
            ).values('id', 'qtNaCesta')

        for cesta in itensCesta:

            qtProducao = cesta.get('qtNaCesta') * cestasCompletas

            doacoes = DoacaoRecebida.objects.annotate(
                    diasValidade = ExpressionWrapper(
                        F('dataValidade') - datetime.now().date(),
                        output_field=IntegerField()
                    ) / 1000000 * 60 * 60 * 24,
                    qtRecebido = F('quantidade') * F('produto__qtdeNaEmbalagem')
                ).select_related(
                    'produto__grupoProduto'
                ).filter(
                    dataRecebimento__gte = datetime.now() - timedelta(60),
                    diasValidade__gte = F('produto__grupoProduto__diasValidadeMinima'),
                    status = 'EST',
                    produto__grupoProduto = cesta.get('id')
                ).order_by(
                    'dataValidade'
                ).values('id', 'quantidade', 'produto__qtdeNaEmbalagem')

            insert_list = []
            update_list = []

            for doacao in doacoes:

                qtProducao -= doacao.get('quantidade') * doacao.get('produto__qtdeNaEmbalagem')
                
                if qtProducao < 0:
                    qtProducao = qtProducao / doacao.get('produto__qtdeNaEmbalagem') * -1
                    insert_list.append([doacao.get('id'), qtProducao])
                
                update_list.append(doacao.get('id'))

                if qtProducao <= 0: break

            DoacaoRecebida.objects.filter(
                    pk__in = update_list
                ).update(
                    status = 'ENT', 
                    dataBaixa = datetime.now()
                )

            insercoes = []
            for doacao in insert_list:
                r = DoacaoRecebida.objects.get(pk = doacao[0])
                r.quantidade = doacao[1]
                r.dataBaixa = None
                r.status = 'EST'
                r.id = None
                r.doacaoAgendada = None
                r.saldoDeEntrega = True
                insercoes.append(r)

            if insercoes:
                DoacaoRecebida.objects.bulk_create(insercoes)

        DoacaoAgendada.objects.filter(
            dataAgendamento__range = [
                datetime.now().date() - timedelta(60),
                datetime.now().date() - timedelta(DoacaoService.ORG.diasEsperaAgendadas + 1)
            ],
            status = 'PEN'
        ).update(
            status = 'CAN'
        )



    def getById(self, pk):
        return DoacaoAgendada.objects.get(pk=pk)



    def listByDoador(self, nome):
        return DoacaoAgendada.objects.get_queryset().filter(
                Q(dataAgendamento__gte = DoacaoService.__getDataBaseAgendadas(),
                status = 'PEN') & Q(doador__username__istartswith = nome)
            ).order_by(Lower('doador__username'))



    def listByProduto(self, descricao):
        return DoacaoAgendada.objects.get_queryset().filter(
                Q(dataAgendamento__gte = DoacaoService.__getDataBaseAgendadas(), 
                status = 'PEN') & Q(produto__descricao__istartswith = descricao)
            ).order_by(Lower('produto__descricao'))



    def listAll():
        return DoacaoAgendada.objects.get_queryset().filter(
                Q(dataAgendamento__gte = DoacaoService.__getDataBaseAgendadas(),
                status = 'PEN')
            ).order_by(Lower('produto__descricao'))



    def listProdutoRecebimentos(self, pk):
        return DoacaoRecebida.objects.get_queryset().filter(
                Q(dataRecebimento__gte = datetime.now() - timedelta(60),
                produto__grupoProduto = pk)
            ).order_by('dataRecebimento')



    def listProdutoAgendados(self, pk):
        return DoacaoAgendada.objects.get_queryset().filter(
                Q(dataAgendamento__gte = DoacaoService.__getDataBaseAgendadas(),
                produto__grupoProduto = pk)
            ).order_by('dataAgendamento')



    def getNomeGrupoProduto(self, pk):
        dict = GrupoProduto.objects.filter(pk=pk).values('descricao')
        return dict[0].get('descricao') if len(dict) != 0 else None


    def itensCestas():

        itensCesta = GrupoProduto.objects.filter(
                compoeCesta = True
            ).annotate(
                esperado = F('qtdeNaEmbalagem') * F('unidadesNaCesta') * DoacaoService.ORG.metaQtdeCestas, 
                qtdeEmbalagem = F('qtdeNaEmbalagem'),
                unidNaCesta = F('unidadesNaCesta'),
                agendado = Value(0),
                recebido = Value(0),
                percentual = Value(0)
            ).order_by('descricao')

        itensDoados = DoacaoRecebida.objects.annotate(
            diasValidade = ExpressionWrapper(
                F('dataValidade') - datetime.now().date(),
                output_field=IntegerField()
            ) / (1000000 * 60 * 60 * 24)
        ).filter(
            dataRecebimento__gte = DoacaoService.__getDataBaseRecebidas(),
            diasValidade__gte = F('produto__grupoProduto__diasValidadeMinima'),
            status = 'EST'
        ).values(
            'produto__grupoProduto'
        ).annotate(
            soma = Sum(F('quantidade') * F('produto__qtdeNaEmbalagem')), 
            tipo = Value('R')
        ).union(
            DoacaoAgendada.objects.filter(
                dataAgendamento__gte = DoacaoService.__getDataBaseAgendadas(),
                status = 'PEN'
            ).values(
                'produto__grupoProduto'
            ).annotate(
                soma = Sum(F('quantidade') * F('produto__qtdeNaEmbalagem')),
                tipo = Value('A')
            ), 
            all = True
        ).order_by('produto__grupoProduto')

        for cesta in itensCesta:
            for doado in itensDoados:
                if doado.get('produto__grupoProduto') > cesta.id: break
                
                if doado.get('produto__grupoProduto') == cesta.id:
                    if doado.get('tipo') == 'A':
                        cesta.agendado += doado.get('soma') / cesta.qtdeEmbalagem
                    else:
                        cesta.recebido += doado.get('soma') / cesta.qtdeEmbalagem

                cesta.percentual = int((cesta.agendado + cesta.recebido) * cesta.qtdeEmbalagem / cesta.esperado * 100)

        return itensCesta



    def cestas():

        itensCesta = DoacaoService.itensCestas()

        cestasCompletas = cestasAgendadas = 999999

        for cesta in itensCesta:

            qtd = int(cesta.agendado / cesta.unidNaCesta)
            if qtd < cestasAgendadas: cestasAgendadas = qtd

            qtd = int(cesta.recebido / cesta.unidNaCesta)
            if qtd < cestasCompletas: cestasCompletas = qtd

        return cestasCompletas, cestasAgendadas, itensCesta



    def __getDataBaseAgendadas():
        return datetime.now().date() - timedelta(DoacaoService.ORG.diasEsperaAgendadas)



    def __getDataBaseRecebidas():
        return datetime.now().date() - timedelta(DoacaoRecebida.DIAS_INICIO_PERIODO)



    def __getQtdeCestasCompletas():
        return DoacaoRecebida.objects.annotate(
                diasValidade = ExpressionWrapper(
                    F('dataValidade') - datetime.now().date(),
                    output_field=IntegerField()
                ) / 1000000 * 60 * 60 * 24
            ).filter(
                dataRecebimento__gte = datetime.now() - timedelta(60),
                diasValidade__gte = F('produto__grupoProduto__diasValidadeMinima'),
                status = 'EST',
                produto__grupoProduto__compoeCesta = True
            ).values(
                'produto__grupoProduto'
            ).annotate(
                qtRecebido = Sum(F('quantidade') * F('produto__qtdeNaEmbalagem')),
                qtNaCesta= F('produto__grupoProduto__qtdeNaEmbalagem') * F('produto__grupoProduto__unidadesNaCesta')
            ).aggregate(
                cestas=Cast(Min(F('qtRecebido') / F('qtNaCesta')), IntegerField())
            ).get('cestas')
