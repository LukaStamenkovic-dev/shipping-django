from django.contrib import admin, messages
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from ..models import Profile, VehicleLog
from .vehicle import VehicleInline
from .vehicle_log import VehicleLogInline


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, VehicleInline, VehicleLogInline, )

    def save_formset(self, request, form, formset, change):
        # 1. Profil i vozilo cuvamo normalno, kao i do sada
        if formset.model != VehicleLog:
            super().save_formset(request, form, formset, change)
            return

        # 2. Korisnik cija se stranica cuva
        user = form.instance

        # 3. Napravi logove, ali ih JOS NE upisuj u bazu
        logs = formset.save(commit=False)

        # 4. Obrisi logove kojima je stikliran "Delete"
        for log in formset.deleted_objects:
            log.delete()

        # 5. Svakom NOVOM logu upisi vozilo korisnika, pa ga sacuvaj
        for log in logs:
            if log.vehicle_id is None:
                if not hasattr(user, 'vehicle'):
                    messages.error(request, f"{user.username} nema dodeljeno vozilo, log nije sačuvan.")
                    continue
                log.vehicle = user.vehicle
            log.save()


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)