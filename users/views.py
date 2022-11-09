from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from users.forms import RegisterForm
from django.urls import reverse_lazy


class SignUp(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
class ProfileDetailView(DetailView):
    model = 'users.User'
    template_name = 'profile.html'
    context_object_name = 'profiles'