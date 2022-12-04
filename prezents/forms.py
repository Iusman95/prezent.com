from django import forms
from django.core import validators
from user_profile.models import Files
from prezents.models import Post, Comment
    


class DowlandFileForm(forms.ModelForm):
    file = forms.FileField(label='файл',
    validators=[validators.FileExtensionValidator(
        allowed_extensions=('docx', 'pptx'))], 
        error_messages={
            'invalid_extension': 'Этот формат не поддерживается'})


    title = forms.CharField(label='Описание', 
                            widget=forms.widgets.TextInput())
    

    class Meta:
        model = Files
        fields = ['file', 'title']

class CreatePostForm(forms.ModelForm):
    file = forms.FileField(label='файл',
    validators=[validators.FileExtensionValidator(
        allowed_extensions=('docx', 'pptx'))], 
        error_messages={
            'invalid_extension': 'Этот формат не поддерживается'})
    
    description = forms.Textarea() 
                            
    class Meta:
        model = Post
        fields = ['file', 'description']


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment    
        fields = ['title', ]