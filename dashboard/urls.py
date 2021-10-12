from django.urls import path

from .views import DashboardView, FechaCestaView, FechaCestaUpdate

app_name = 'dashboard'

urlpatterns = [
    path('', DashboardView.as_view(), name='view'),
    path('f3ch4_c3$t4_n2p@a&fn8i3n', FechaCestaView.as_view(), name="fcesta"),
    path('f3ch4_c3$t4_n3r@aw8i0$4x', FechaCestaUpdate.as_view(), name="updcesta")
]
