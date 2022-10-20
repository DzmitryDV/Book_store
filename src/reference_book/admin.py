from django.contrib import admin

from . import models

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('pk','surname', 'name', 'patronymic')

admin.site.register(models.BookAuthor, AuthorAdmin)
admin.site.register(models.BookGenre)
admin.site.register(models.BookPublisher)
admin.site.register(models.BookSerie)
admin.site.register(models.Currency)