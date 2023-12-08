# app/views.py

from rest_framework import generics, viewsets, permissions
from rest_framework.response import Response
from rest_framework import status

from app.models import Device, TelemetryData
from .serializers import DeviceSerializer, TelemetryDataSerializer, UserSerializer

from rest_framework_simplejwt.tokens import RefreshToken

class UserRegistrationView(generics.CreateAPIView):
    """
    API view for user registration.

    Creates a new user using the provided data, generates refresh and access tokens,
    and returns the tokens in the response upon successful registration.
    """
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        """
        Handle POST requests for user registration.

        Returns a response containing refresh and access tokens upon successful registration.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        refresh = RefreshToken.for_user(user)
        response_data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

        return Response(response_data, status=status.HTTP_201_CREATED)
    

class DeviceViewSet(viewsets.ModelViewSet):
    """
    API viewset for managing devices.

    Performs CRUD operations on Device objects, utilizing the DeviceSerializer for data representation.
    Requires authentication for access.
    """
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [permissions.IsAuthenticated]


class TelemetryDataViewSet(viewsets.ModelViewSet):
    """
    API viewset for managing telemetry data.

    Performs CRUD operations on TelemetryData objects, utilizing the TelemetryDataSerializer for data representation.
    Requires authentication for access.
    """
    queryset = TelemetryData.objects.all()
    serializer_class = TelemetryDataSerializer
    permission_classes = [permissions.IsAuthenticated]
