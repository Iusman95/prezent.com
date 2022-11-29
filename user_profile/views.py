from users.models import User
from django.views.generic import DetailView, UpdateView
from django.urls import reverse


# Create your views here.


#Представление  для Профиля
class ProfileDetailView(DetailView):
    model = User
    template_name = 'profile/profile.html'
    


#Представление для обнавления данных на профиле 
class ProfileCreateView(UpdateView):
    model = User
    template_name = 'profile/create_profile.html'
    fields = ['username', 'first_name', 'last_name', 'email', 'description']
    

    def get_success_url(self):
           pk = self.kwargs["pk"]
           return reverse("user_profile", kwargs={"pk": pk})
    
   

        


        




