from django.shortcuts import render
from users.models import User
from user_profile.models import DowlandFile
from django.views.generic import  DetailView, UpdateView, CreateView
from django.urls import reverse
from user_profile.forms import DowlandFileForm, ProfileForm
from django.shortcuts import redirect


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
    
   

        

#Представление для загрузки фотографий на профиль
def add_image_on_profile(request):
    if request.method == "POST":
        form2 = DowlandFileForm(request.POST, request.FILES)
        if form2.is_valid():
            form2.save()
            return redirect('user_profile')
    else:
        form2 = DowlandFileForm()
    
    return render(request, 'profile/create_profile.html', {'form2': form2})
        




