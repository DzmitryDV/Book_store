from django.db import models
from django.urls import reverse_lazy

# Create your models here.

class BookAuthor(models.Model):
    name = models.CharField(
        max_length=40,
        verbose_name="Имя",
        )
    surname = models.CharField(
        max_length=40,
        verbose_name="Фамилия",
        )
    patronymic = models.CharField(
        max_length=40,
        verbose_name="Отчество",
        blank=True,
        null=True,
        )
    def __str__(self) -> str:
        if self.patronymic == None:
            return f'{self.surname} {self.name}'
        else:
             return f'{self.surname} {self.name} {self.patronymic}'  
    def get_absolute_url(self):
        #return f'/show_author/{self.pk}/'
        return reverse_lazy('reference_book:author-detail', kwargs={'pk': self.pk})
    
class BookSerie(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Серия",
        
        )
    def __str__(self) -> str:
        return self.name
    def get_absolute_url(self):
        #return f'/show_serie/{self.pk}/'
        return reverse_lazy('reference_book:serie-detail', kwargs={'pk': self.pk}) 

class BookGenre(models.Model):
    name = models.CharField(
        max_length=40,
        verbose_name="Жанр",
        )
    description = models.TextField(
        verbose_name="Описание жанра",
        blank=True,
        null=True,
    )
    def __str__(self) -> str:
        return self.name
    def get_absolute_url(self):
        #return f'/show_genre/{self.pk}/'
        return reverse_lazy('reference_book:genre-detail', kwargs={'pk': self.pk})

class BookPublisher(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Издательство",
        
        )
    def __str__(self) -> str:
        return self.name
    def get_absolute_url(self):
        #return f'/show_publisher/{self.pk}/'
        return reverse_lazy('reference_book:publisher-detail', kwargs={'pk': self.pk})

class Currency(models.Model):
    name = models.CharField(
        default="BYN",
        max_length=5,
        verbose_name="Валюта"
    )
    description = models.CharField(
        max_length=40,
        default="Белорусский рубль",
        verbose_name="Наименование валюты"
    )
    def __str__(self) -> str:
        return f'{self.name} - "{self.description}"'
    def get_absolute_url(self):
        #return f'/show_currency/{self.pk}/'
        return reverse_lazy('reference_book:currency-detail', kwargs={'pk': self.pk})
