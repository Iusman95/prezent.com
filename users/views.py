from django.views.generic import CreateView, DetailView
from users.forms import RegisterUserForm
from django.urls import reverse_lazy
from django.shortcuts import redirect
from users.models import User


class SignUp(CreateView):
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'






    

