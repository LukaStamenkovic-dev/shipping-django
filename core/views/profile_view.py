from django.shortcuts import redirect
from django.views.generic import DetailView
from django.utils import timezone

from ..forms import VehicleLogForm
from ..models import Profile, VehicleLog

class ProfileView(DetailView):
    model = Profile
    template_name = 'profile.html'
    context_object_name = 'data'

    def get_object(self, queryset = None):
        return Profile.objects.get(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        today = timezone.localdate()

        already_logged = VehicleLog.objects.filter(
            user = self.request.user,
            return_time__date=today
        )

        context['already_logged'] = already_logged

        if not already_logged:
            context['form'] = VehicleLogForm()

        return context

    def post(self, request, *args, **kwargs):
        today = timezone.localdate()

        already_logged = VehicleLog.objects.filter(
            user = self.request.user,
            return_time__date=today
        )

        if not already_logged:
            return redirect('profile')

        form = VehicleLogForm(request.POST)

        if form.is_valid():
            log = form.save(commit=False)

            log.user = request.user
            log.vehicle = request.user.vehicle
            log.return_time = timezone.now()

            log.save()

            return redirect('profile')