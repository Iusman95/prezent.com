from django.shortcuts import render, redirect
from prezents.forms import DowlandFileForm, CreatePostForm
from user_profile.models import Files
from prezents.models import Post


#Представление для главной страницы для вывода всех загруженных данных 
def index(request):
    posts = Post.objects.all()
    return render(request, 
        template_name='prezents/index.html',
        context={'posts': posts})


#Представление для страницы "my_files"
def my_files(request):
    files = Files.objects.filter(user=request.user)
    return render(request, 
        template_name='prezents/my_files.html', 
        context={'files': files})


#Представление для загрузки фотографий на профиль
def add_image_on_profile(request):
    if request.method == "POST":
        form_two = DowlandFileForm(request.POST, request.FILES)
        if form_two.is_valid():
            form_two.instance.user = request.user
            form_two.save()
            return redirect('my_files')
    else:
        form_two = DowlandFileForm()
    
    return render(request, 
        template_name='prezents/upload_file.html', 
        context={'form_two': form_two})

#Представление для сохранение поста
def add_post(request):
    if request.method == "POST":
        form_ = CreatePostForm(request.POST, request.FILES)
        if form_.is_valid():
            form_.instance.user = request.user
            form_.save()
            return redirect('index')
    else:
        form_ = CreatePostForm()
    
    return render(request, 
        template_name='prezents/upload_index.html', 
        context={'form_': form_})
        
