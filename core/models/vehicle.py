from django.contrib.auth.models import User
from django.db import models


class Vehicle(models.Model):
    VEHICLE_TYPE = (
        ('truck', 'Truck'),
        ('van', 'Van'),
        ('car', 'Car'),
    )

    STATUS_CHOICES = (
        ('available', 'Available'),
        ('in_use', 'In use'),
        ('maintenance', 'Maintenance'),
        ('inactive', 'Inactive'),
    )

    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_TYPE)
    plate_number = models.CharField(max_length=20, unique=True)
    brand = models.CharField(max_length=32)
    model = models.CharField(max_length=32)
    year = models.PositiveIntegerField()
    mileage = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    user = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='vehicle',
    )
    workhours = models.PositiveIntegerField(default=0)
    capacity = models.FloatField(help_text='Max load in kg')

    def __str__(self):
        return f"{self.plate_number} ({self.vehicle_type})"