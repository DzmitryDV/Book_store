from . import models, forms
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

def index(request):
    return render(request, 'reference_book/index.html')

class Author():

    class ListAuthor(generic.ListView):
        model = models.BookAuthor
        template_name='reference_book/list_author.html'
        def get_context_data(self, *args, **kwargs):
            context = super().get_context_data(*args, **kwargs)
            context ['operation_name'] = 'reference_book:author-detail'
            return context
    
    class ShowAutor(generic.DetailView):
        model = models.BookAuthor
        template_name='reference_book/detail_author.html'

    class CreateAuthor(generic.CreateView):
        model = models.BookAuthor
        form_class = forms.BookAuthorForm  
        template_name='reference_book/edit_author.html'
        def get_context_data(self, *args, **kwargs):
            context = super().get_context_data(*args, **kwargs)
            context ['operation_name'] = 'Добавить автора' 
            return context

    class UpdateAuthor(generic.UpdateView):
        model = models.BookAuthor
        form_class = forms.BookAuthorForm  
        template_name='reference_book/edit_author.html'
        def get_context_data(self, *args, **kwargs):
            context = super().get_context_data(*args, **kwargs)
            context ['operation_name'] = 'Редактировать автора' 
            return context

    class DeleteAuthor(generic.DeleteView):
        model = models.BookAuthor
        template_name='reference_book/delete_author.html'
        success_url = reverse_lazy('reference_book:authors-list')                                                     

class BkSerie():
    class ListSerie(generic.ListView):
        model = models.BookSerie
        template_name='reference_book/list_serie.html' 

    class ShowSerie(generic.DetailView):
        model = models.BookSerie
        template_name='reference_book/detail_serie.html'

    class CreateSerie(generic.CreateView):
        model = models.BookSerie
        form_class = forms.BookSerieForm  
        template_name='reference_book/edit_serie.html'
        def get_context_data(self, *args, **kwargs):
            context = super().get_context_data(*args, **kwargs)
            context ['operation_name'] = 'Добавить серию' 
            return context

    class UpdateSerie(generic.UpdateView):
        model = models.BookSerie
        form_class = forms.BookSerieForm  
        template_name='reference_book/edit_serie.html'
        def get_context_data(self, *args, **kwargs):
            context = super().get_context_data(*args, **kwargs)
            context ['operation_name'] = 'Редактировать серию' 
            return context

    class DeleteSerie(generic.DeleteView):
        model = models.BookSerie
        template_name='reference_book/delete_serie.html'
        #success_url = '/show_series/'
        success_url = reverse_lazy('reference_book:series-list')

class BkGenre():
    class ListGenre(generic.ListView):
        model = models.BookGenre
        template_name='reference_book/list_genre.html' 

    class ShowGenre(generic.DetailView):
        model = models.BookGenre
        template_name='reference_book/detail_genre.html'

    class CreateGenre(generic.CreateView):
        model = models.BookGenre
        form_class = forms.BookGenreForm
        template_name='reference_book/edit_genre.html'
        def get_context_data(self, *args, **kwargs):
            context = super().get_context_data(*args, **kwargs)
            context ['operation_name'] = 'Добавить жанр' 
            return context

    class UpdateGenre(generic.UpdateView):
        model = models.BookGenre
        form_class = forms.BookGenreForm
        template_name='reference_book/edit_genre.html'
        def get_context_data(self, *args, **kwargs):
            context = super().get_context_data(*args, **kwargs)
            context ['operation_name'] = 'Редактировать жанр' 
            return context

    class DeleteGenre(generic.DeleteView):
        model = models.BookGenre
        template_name='reference_book/delete_genre.html'
        #success_url = '/show_genres/'
        success_url = reverse_lazy('reference_book:genres-list')

class BkPublisher():
    class ListPublisher(generic.ListView):
        model = models.BookPublisher
        template_name='reference_book/list_publisher.html' 

    class ShowPublisher(generic.DetailView):
        model = models.BookPublisher
        template_name='reference_book/detail_publisher.html'

    class CreatePublisher(generic.CreateView):
        model = models.BookPublisher
        form_class = forms.BookPublisherForm
        template_name='reference_book/edit_publisher.html'
        def get_context_data(self, *args, **kwargs):
            context = super().get_context_data(*args, **kwargs)
            context ['operation_name'] = 'Добавить издательство' 
            return context

    class UpdatePublisher(generic.UpdateView):
        model = models.BookPublisher
        form_class = forms.BookPublisherForm
        template_name='reference_book/edit_publisher.html'
        def get_context_data(self, *args, **kwargs):
            context = super().get_context_data(*args, **kwargs)
            context ['operation_name'] = 'Редактировать издательство' 
            return context

    class DeletePublisher(generic.DeleteView):
        model = models.BookPublisher
        template_name='reference_book/delete_publisher.html'
        #success_url = '/show_publishers/'
        success_url = reverse_lazy('reference_book:publishers-list')

class BkCurrency():
    class ListCurrency(generic.ListView):
        model = models.Currency
        template_name='reference_book/list_currency.html' 

    class ShowCurrency(generic.DetailView):
        model = models.Currency
        template_name='reference_book/detail_currency.html'

    class CreateCurrency(generic.CreateView):
        model = models.Currency
        form_class = forms.CurrencyForm
        template_name='reference_book/edit_currency.html'
        def get_context_data(self, *args, **kwargs):
            context = super().get_context_data(*args, **kwargs)
            context ['operation_name'] = 'Добавить валюту' 
            return context

    class UpdateCurrency(generic.UpdateView):
        model = models.Currency
        form_class = forms.CurrencyForm
        template_name='reference_book/edit_currency.html'
        def get_context_data(self, *args, **kwargs):
            context = super().get_context_data(*args, **kwargs)
            context ['operation_name'] = 'Редактировать валюту' 
            return context

    class DeleteCurrency(generic.DeleteView):
        model = models.Currency
        template_name='reference_book/delete_currency.html'
        #success_url = 'refs/show_currencys/'
        success_url = reverse_lazy('reference_book:currencys-list')




