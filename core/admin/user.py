from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from ..models import Profile, VehicleLog, Vehicle
from .vehicle import VehicleInline
from .vehicle_log import VehicleLogInline


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, VehicleInline, VehicleLogInline, )

    def save_formset(self, request, form, formset, change):

        instances = formset.save(commit=False)

        for instance in instances:
            if isinstance(instance, VehicleLog):
                vehicle = Vehicle.objects.filter(user=form.instance).first()

                if vehicle:
                    instance.vehicle = vehicle

            instance.save()

        formset.save_m2m()


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)