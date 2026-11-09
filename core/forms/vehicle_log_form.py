from django import forms

from ..models import VehicleLog


class VehicleLogForm(forms.ModelForm):

    class Meta:
        model = VehicleLog
        fields = ['mileage', ]
