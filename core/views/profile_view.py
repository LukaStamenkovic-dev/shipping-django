from django.shortcuts import redirect
from django.views.generic import DetailView
from django.utils import timezone

from ..forms import VehicleLogForm
from ..models import Profile, VehicleLog
from ..services import VehicleLogService

class ProfileView(DetailView):
    model = Profile
    template_name = 'profile.html'
    context_object_name = 'data'

    def get_object(self, queryset = None):
        return Profile.objects.get(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        state = VehicleLogService.get_state(self.request.user)

        if state['vehicle'] is None:
            context['has_vehicle'] = False
            return context

        context['already_logged'] = state['already_logged']

        if not state['already_logged']:
            context['form'] = VehicleLogForm()

        return context

    def post(self, request, *args, **kwargs):
        state = VehicleLogService.get_state(self.request.user)

        if state['vehicle'] is None or state['already_logged']:
            return redirect('profile')

        form = VehicleLogForm(request.POST)

        if form.is_valid():
            log = form.save(commit=False)

            log.user = request.user
            log.vehicle = request.user.vehicle
            log.return_time = timezone.now()

            log.save()

            return redirect('profile')