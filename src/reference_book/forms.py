from django import forms
from . import models

class BookAuthorForm(forms.ModelForm):
    class Meta:
        model = models.BookAuthor
        fields = [
            'surname',
            'name', 
            'patronymic'
        ]
        # fields = '__all__' (если нужно добавить все поля модели)
    
     
