from pages.models import FamiliaAtendida
from django.db.models import Sum, Q

class FamiliaAtendidaService():
    
    def getMetaCestas():
        cestas = FamiliaAtendida.objects.filter(ativo=True).aggregate(
            cestas=Sum('qtdeCestas')
        )['cestas']
        
        return 1 if cestas is None else cestas
        
    def getCestasNoPeriodo(dataInicial, dataFinal):
        """
        SELECT SUM(qtde_cestas) 
            FROM familia_atendida 
            WHERE (ativo=true OR dataDesativacao >= PARAM:data_final)
                        AND data_cadastro >= PARAM:data_inicial
        """
        cestas = FamiliaAtendida.objects.filter(
            Q(ativo=True) | Q(dataDesativacao__gte = dataFinal), 
            dataCadastro__gte = dataInicial
        ).aggregate(
            cestas=Sum('qtdeCestas')
        )['cestas']

        return 0 if cestas is None else cestas
