from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.shortcuts import redirect
from django.http import HttpResponse

from services.doacao_service import DoacaoService

class DashboardView(GroupRequiredMixin, LoginRequiredMixin, TemplateView):

    template_name = 'dashboard/dashboard.html'
    group_required = 'admin_users'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)

        cestas = DoacaoService.cestas()

        context['cestasCompletas'] = cestas[0]
        context['cestasAgendadas'] = cestas[1]
        context['db'] = cestas[2]

        return context



class FechaCestaView(GroupRequiredMixin, LoginRequiredMixin, TemplateView):

    template_name = 'dashboard/fecha_ok.html'
    group_required = 'admin_users'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):

        context = super(FechaCestaView, self).get_context_data(**kwargs)
        cestas = DoacaoService.cestas()
        context['cestasCompletas'] = cestas[0]

        return context



class FechaCestaUpdate(GroupRequiredMixin, LoginRequiredMixin, View):

    group_required = 'admin_users'
    redirect_field_name = 'redirect_to'

    def post(self, request):
        DoacaoService.fecharCestas()
        return redirect('dashboard:view')
        