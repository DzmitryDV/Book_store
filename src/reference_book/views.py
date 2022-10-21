from . import models, forms
from django.views import generic


class Author():

    class ListAuthor(generic.ListView):
        model = models.BookAuthor
        template_name='reference_book/list_author.html'
    
    class ShowAutor(generic.DetailView):
        model = models.BookAuthor
        template_name='reference_book/detail_author.html'

    class CreateAuthor(generic.CreateView):
        model = models.BookAuthor
        form_class = forms.BookAuthorForm  
        template_name='reference_book/create_author.html' 

    class UpdateAuthor(generic.UpdateView):
        model = models.BookAuthor
        form_class = forms.BookAuthorForm  
        template_name='reference_book/update_author.html'

    class DeleteAuthor(generic.DeleteView):
        model = models.BookAuthor
        template_name='reference_book/delete_author.html'
        success_url = '/show_authors/'    

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
        template_name='reference_book/create_serie.html'

    class UpdateSerie(generic.UpdateView):
        model = models.BookSerie
        form_class = forms.BookSerieForm  
        template_name='reference_book/update_serie.html'

    class DeleteSerie(generic.DeleteView):
        model = models.BookSerie
        template_name='reference_book/delete_serie.html'
        success_url = '/show_series/'

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
        template_name='reference_book/create_genre.html'

    class UpdateGenre(generic.UpdateView):
        model = models.BookGenre
        form_class = forms.BookGenreForm
        template_name='reference_book/update_genre.html'

    class DeleteGenre(generic.DeleteView):
        model = models.BookGenre
        template_name='reference_book/delete_genre.html'
        success_url = '/show_genres/'

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
        template_name='reference_book/create_publisher.html'

    class UpdatePublisher(generic.UpdateView):
        model = models.BookPublisher
        form_class = forms.BookPublisherForm
        template_name='reference_book/update_publisher.html'

    class DeletePublisher(generic.DeleteView):
        model = models.BookPublisher
        template_name='reference_book/delete_publisher.html'
        success_url = '/show_publishers/'

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
        template_name='reference_book/create_currency.html'

    class UpdateCurrency(generic.UpdateView):
        model = models.Currency
        form_class = forms.CurrencyForm
        template_name='reference_book/update_currency.html'

    class DeleteCurrency(generic.DeleteView):
        model = models.Currency
        template_name='reference_book/delete_currency.html'
        success_url = '/show_currencys/'




