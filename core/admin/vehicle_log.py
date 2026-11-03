from django.contrib import admin
from ..models import VehicleLog


class VehicleLogInline(admin.StackedInline):
    model = VehicleLog
    extra = 1

    exclude = ['vehicle']

    def has_add_permission(self, request, obj=None):
        # TODO: return True or False
        # hint: can a new log be added from the user page?
        pass

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        # TODO: return True or False
        pass