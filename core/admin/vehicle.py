from django.contrib import admin
from ..models import Vehicle


class VehicleInline(admin.StackedInline):
    model = Vehicle
    max_num = 1