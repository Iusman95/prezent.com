from django.urls import path
from . import views

urlpatterns = [
   path('user_profile/<int:pk>/', views.ProfileDetailView.as_view(), name='user_profile'),
   path('edit_profile/<int:pk>/', views.ProfileCreateView.as_view(), name='create_profile'),
   ]