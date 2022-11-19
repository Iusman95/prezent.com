from django.shortcuts import render
from users.models import User
from django.views.generic import  DetailView, UpdateView
from django.urls import reverse_lazy
from django.urls import reverse


# Create your views here.


class ProfileDetailView(DetailView):
    model = User
    template_name = 'profile/profile.html'
    
class ProfileCreateView(UpdateView):
    model = User
    template_name = 'profile/create_profile.html'
    fields = ['username', 'description', ]

    def get_success_url(self):
           pk = self.kwargs["pk"]
           return reverse("user_profile", kwargs={"pk": pk})
