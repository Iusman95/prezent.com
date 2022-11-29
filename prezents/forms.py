from django import forms
from django.core import validators
from user_profile.models import Files
    


class DowlandFileForm(forms.ModelForm):
    file = forms.ImageField(label='Изображение',
    validators=[validators.FileExtensionValidator(
        allowed_extensions=('gif', 'jpg', 'png'))], 
        error_messages={
            'invalid_extension': 'Этот формат не поддерживается'})

    title = forms.CharField(label='Описание', 
                            widget=forms.widgets.Textarea())
    

    class Meta:
        model = Files
        fields = ['file', 'title']

    
     