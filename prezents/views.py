from turtle import title
from django.shortcuts import render, get_object_or_404
from users.models import User
from prezents.models import Prezentation
from django.views.generic import ListView, DetailView, CreateView

class PostListView(ListView):
    model = Prezentation
    template_name = 'prezents/index.html'
    context_object_name = 'prezents'



    