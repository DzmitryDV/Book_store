from . import models, forms
from django.views import generic


class BookAuthor():

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

    

    



