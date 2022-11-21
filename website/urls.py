"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt import views as jwt_views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

"""
Documentação da API
"""
schema_view = get_schema_view(
   openapi.Info(
      title="API Doação",
      default_version='v1',
      description='API de doação a partir de módulo "client" de terceiros',
      #terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@dummy.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('dashboard/', include('dashboard.urls', namespace='dashboard')),
    path('doacao/', include('doacao.urls', namespace='doacao')),
    path('recebimento/', include('recebimento.urls', namespace='recebimento')),
    path('cadastros/', include('cadastros.urls', namespace='cadastros')),
    path('api/v1/doacao/', include('doacaoapi.urls', namespace='doacaoapi')),

    # JWT Authentication
	path(
        'api/token/', 
        jwt_views.TokenObtainPairView.as_view(), 
        name ='token_obtain_pair'
    ),
	path(
        'api/token/refresh/', 
        jwt_views.TokenRefreshView.as_view(), 
        name ='token_refresh'
    ),
    path(
        'api/token/verify/', 
        jwt_views.TokenVerifyView.as_view(), 
        name ='token_verify'
    ),

    # API Documentation
    path('playground', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('docs', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # deixar por último
    path('', include('pages.urls', namespace='pages')),
]
