from django.urls import path
from users.views import ProfileDetailView, SignUp


urlpatterns = [
    path('profile/<int:pk>', ProfileDetailView.as_view(), name='profile'),
    path('signup/', SignUp.as_view(), name='signup'),
]