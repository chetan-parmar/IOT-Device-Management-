from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """
    Custom user model that extends the AbstractUser.

    Adds a 'role' field to represent user roles, with predefined choices.
    Default role is set to 'LEV_MANAGER'.
    """
    USER_ROLES = [
        ('LEV_OPERATOR', 'Level Operator'),
        ('LEV_ENGINEER', 'Level Engineer'),
        ('LEV_MANAGER', 'Level Manager'),
        ('OWNER', 'Owner'),
    ]

    role = models.CharField(choices=USER_ROLES, max_length=20, default='LEV_MANAGER')

    def __str__(self):
        """
        Returns the username as the string representation of the user.
        """
        return self.username
    

class Device(models.Model):
    """
    Model representing a device.

    Attributes:
        name (str): The name of the device.
        description (str): A description of the device.
        created_at (datetime): The timestamp when the device was created.
        telemetry_data (JSONField): JSON field for storing telemetry data (nullable and blank).
    """
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    telemetry_data = models.JSONField(null=True, blank=True)

    def __str__(self):
        """
        Returns the name of the device as its string representation.
        """
        return self.name
    

class TelemetryData(models.Model):
    """
    Model representing telemetry data for a device.

    Attributes:
        device_id (int): Primary key representing the device associated with the telemetry data.
        timestamp (datetime): The timestamp of the telemetry data.
        value (float): The value of the telemetry data.
    """
    device_id = models.IntegerField(primary_key=True)
    timestamp = models.DateTimeField()
    value = models.FloatField()

    class Meta:
        db_table = 'telemetry_data'