"""
Main URL configuration for the Django project.
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

"""
Includes Swagger and ReDoc documentation views:
- '/swagger/' for Swagger UI documentation.
- '/redoc/' for ReDoc documentation.
Utilizes drf_yasg for automatic generation of Swagger documentation.
"""
schema_view = get_schema_view(
   openapi.Info(
      title="Iot device management API",
      default_version='v1',
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

swagger_urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

"""
Defines paths and routes for:
- Django admin interface.
- 'app/' for the 'app' app API views.
- 'api/token/' for JWT token obtainment using TokenObtainPairView.
- 'api/token/refresh/' for JWT token refresh using TokenRefreshView.
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('app.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns+=swagger_urlpatterns