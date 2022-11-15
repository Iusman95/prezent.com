from django.shortcuts import render, get_object_or_404
from profiles.models import Profile
from django.views.generic import DetailView, CreateView
from django.urls import reverse_lazy

class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'base/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context

   

class CreateProfilePageView(CreateView):
    model = Profile
    
    template_name = 'base/create_profile.html'
    fields = ['profile_pic', 'bio', 'facebook', 'twitter', 'instagram']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('index')
