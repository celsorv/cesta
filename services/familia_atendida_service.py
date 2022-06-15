from pages.models import FamiliaAtendida
from django.db.models import Sum

class FamiliaAtendidaService():
    
    def getMetaCestas():
        cestas = FamiliaAtendida.objects.filter(ativo=True).aggregate(cestas=Sum('qtdeCestas'))['cestas']
        return 0 if cestas is None else cestas
        