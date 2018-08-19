"""api URL Configuration"""

from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from auth.views import RefreshAuthTokenView, ObtainAuthTokenView

schema_view = get_schema_view(
   openapi.Info(
      title="Virtuagym API",
      default_version='v1',
      description="Test task for VirtuaGym",
      contact=openapi.Contact(email="ilyasov.dauren@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   validators=['flex', 'ssv'],
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r'^docs(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api/auth/', ObtainAuthTokenView.as_view()),
    path('api/auth/refresh/', RefreshAuthTokenView.as_view()),
    path('api/user/', include('users.urls')),
    path('api/exercise/', include('exercises.urls')),
    path('api/plan/', include('plans.urls')),
    path('api/day/', include('days.urls')),
    path('', RedirectView.as_view(permanent=False, url='/docs/')),
]

