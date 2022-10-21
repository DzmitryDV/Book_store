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

class BookSerieForm(forms.ModelForm):
    class Meta:
        model = models.BookSerie
        fields = [
            'name', 
        ]

class BookGenreForm(forms.ModelForm):
    class Meta:
        model = models.BookGenre
        fields = [
            'name', 
            'description'
        ]
class BookPublisherForm(forms.ModelForm):
    class Meta:
        model = models.BookPublisher
        fields = [
            'name', 
        ]

class CurrencyForm(forms.ModelForm):
    class Meta:
        model = models.Currency
        fields = [
            'name', 
            'description'
        ]
     
