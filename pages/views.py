from django.views.generic import TemplateView
from django.shortcuts import redirect

from users.models  import User

class HomePageView(TemplateView):
    template_name = 'home.html'

    def dispatch(self, request, *args, **kwargs):

        if self.request.user.is_authenticated:
            adm = User.objects.filter(pk=self.request.user.id).values('administrador')
            if adm[0].get('administrador'):
                return redirect('dashboard/')

        return super(HomePageView, self).dispatch(request, *args, **kwargs)
