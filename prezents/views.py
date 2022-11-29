from django.shortcuts import render, redirect
from prezents.forms import DowlandFileForm
from user_profile.models import Files
# Create your views here.

#Представление для главной страницы для вывода всех загруженных данных 
def index(request):
    return render(request, 
        template_name='prezents/index.html'
        )


#Представление для страницы "my_files"
def my_files(request, ):
    files = Files.objects.filter(user=request.user)
    return render(request, 
        template_name='prezents/my_files.html', 
        context={'files': files})


#Представление для загрузки фотографий на профиль
def add_image_on_profile(request):
    if request.method == "POST":
        data = dict(request.POST)
        form_two = DowlandFileForm(data, request.FILES)
        if form_two.is_valid():
            form_two.instance.user = request.user
            form_two.save()
            return redirect('index')
    else:
        form_two = DowlandFileForm()
    
    return render(request, 
        template_name='prezents/upload_file.html', 
        context={'form_two': form_two})