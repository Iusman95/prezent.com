from django.urls import path
from . import views

urlpatterns = [ 
    path('index/', views.index, name='index'),
    path('upload_file/', views.add_image_on_profile, name='upload_file'),
    path('my_files/', views.my_files, name='my_files'),  
    ]

