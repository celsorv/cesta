from django.contrib import admin

from .models import UnidadeOrganizacao, GrupoProduto, Produto, DoacaoAgendada, DoacaoRecebida

admin.site.register(UnidadeOrganizacao)
admin.site.register(GrupoProduto)
admin.site.register(Produto)
admin.site.register(DoacaoAgendada)
admin.site.register(DoacaoRecebida)
