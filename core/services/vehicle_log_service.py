from django.utils import timezone
from ..models import VehicleLog

class VehicleLogService:

    @staticmethod
    def get_state(user):

        vehicle = getattr(user, 'vehicle', None)

        if vehicle is None:
            return {
                'has_vehicle': False,
                'vehicle': None,
                'already_logged': None
            }

        today = timezone.localdate()

        already_logged = VehicleLog.objects.filter(
            user=user,
            return_time__date=today
        ).exists()

        return {
            'has_vehicle': True,
            'vehicle': vehicle,
            'already_logged': already_logged
        }