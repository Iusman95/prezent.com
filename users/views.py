from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, DetailView
from users.forms import RegisterForm
from django.urls import reverse_lazy
from users.models import User


class SignUp(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'






    

