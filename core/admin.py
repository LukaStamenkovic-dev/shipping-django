from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile, Vehicle, VehicleLog


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class VehicleInline(admin.StackedInline):
    model = Vehicle
    max_num = 1

class VehicleLogInline(admin.TabularInline):
    model = VehicleLog
    extra = 1

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, VehicleInline, VehicleLogInline, )


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

admin.site.register(Vehicle)
admin.site.register(VehicleLog)
