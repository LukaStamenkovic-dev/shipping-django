from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from ..models import Profile
from .vehicle import VehicleInline
from .vehicle_log import VehicleLogInline


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, VehicleInline, VehicleLogInline, )


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
