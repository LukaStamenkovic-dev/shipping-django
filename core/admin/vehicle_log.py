from django.contrib import admin
from ..models import VehicleLog


class VehicleLogInline(admin.StackedInline):
    model = VehicleLog
    extra = 1