# app/urls.py

"""
URL configuration for the 'app' app.

Defines the paths and routes for various API views including:
- '/register/' for user registration using UserRegistrationView.
- '/devices/' for CRUD operations on devices using DeviceViewSet.
- '/telemetry/' for CRUD operations on telemetry data using TelemetryDataViewSet.

Utilizes Django Rest Framework routers for automatic URL routing.
"""

from django.urls import path, include
from rest_framework import routers
from app.views import DeviceViewSet, TelemetryDataViewSet, UserRegistrationView

router = routers.DefaultRouter()
router.register(r'devices', DeviceViewSet)
router.register(r'telemetry', TelemetryDataViewSet)


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('', include(router.urls)),
]
