from django.views.generic import DeleteView
from ..models import Profile

class ProfileView(DeleteView):
    model = Profile
    template_name = 'profile.html'
    context_object_name = 'data'

    def get_object(self, queryset = None):
        return Profile.objects.get(user=self.request.user)