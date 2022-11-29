from django.contrib.auth.forms import UserCreationForm
from users.models import User
from django import forms

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Почта', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пороль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='повторный пороль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-unput'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}), 
            'password1': forms.PasswordInput(attrs={'class':'form-input'}),
            'password2': forms.PasswordInput(attrs={'class':'form-input'}),
        }