from django.urls import path
from prezents.views import  PostListView


urlpatterns = [
     path('index/', PostListView.as_view(), name='index')
]