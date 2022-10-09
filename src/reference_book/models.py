from django.db import models

# Create your models here.

class BookAuthor(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Имя",
        )
    surname = models.CharField(
        max_length=100,
        verbose_name="Фамилия",
        )
    patronymic = models.CharField(
        max_length=100,
        verbose_name="Отчество",
        blank=True,
        null=True,
        )
    def __str__(self) -> str:
        if self.patronymic == None:
            return f'{self.surname} {self.name}'
        else:
             return f'{self.surname} {self.name} {self.patronymic}'  
    
    

class BookSerie(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Серия",
        
        )
    def __str__(self) -> str:
        return self.name

class BookGenre(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Жанр",
        )
    description = models.TextField(
        blank=True,
        null=True,
    )
    def __str__(self) -> str:
        return self.name

class BookPublisher(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Издательство",
        
        )
    def __str__(self) -> str:
        return self.name



