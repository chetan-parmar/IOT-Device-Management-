from rest_framework import serializers
from .models import CustomUser, Device, TelemetryData
"""
Serializers for the CustomUser, Device, and TelemetryData models.
"""

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the CustomUser model, includes 'id', 'username', 'password', and 'role' fields.
    """
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """
        Creates and returns a new CustomUser instance with the validated data.
        """
        user = CustomUser(username=validated_data['username'], role=validated_data['role'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class DeviceSerializer(serializers.ModelSerializer):
    """
    Serializer for the Device model, includes all fields.
    """
    class Meta:
        model = Device
        fields = '__all__'


class TelemetryDataSerializer(serializers.ModelSerializer):
    """
    Serializer for the TelemetryData model, includes all fields.
    """
    class Meta:
        model = TelemetryData
        fields = '__all__'