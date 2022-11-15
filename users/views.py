from django.views.generic import CreateView
from users.forms import RegisterUserForm
from django.urls import reverse_lazy



class SignUp(CreateView):
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'






    

