from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from .vehicle import Vehicle


class VehicleLog(models.Model):
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    mileage = models.PositiveIntegerField()
    return_time = models.DateTimeField(default=timezone.now)
