from operator import mod
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class BookAuthor(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Автор",
        
        )
    def __str__(self) -> str:
        return self.name

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



