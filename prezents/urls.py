from django.urls import path
from prezents.views import index

urlpatterns = [ 
    path('index/', index, name='index'),
    
]


"""   path('upload_file/', upload_file, name='upload_file'), """
