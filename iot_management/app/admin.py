from django.contrib import admin
from .models import CustomUser, Device, TelemetryData

admin.site.register(CustomUser)
admin.site.register(Device)
admin.site.register(TelemetryData)
