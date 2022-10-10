from django.contrib import admin

from . import models

# Register your models here.

admin.site.register(models.BookAuthor)
admin.site.register(models.BookGenre)
admin.site.register(models.BookPublisher)
admin.site.register(models.BookSerie)
admin.site.register(models.Currency)