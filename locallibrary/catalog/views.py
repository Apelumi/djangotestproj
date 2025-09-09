from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic
from django.http import Http404
# Create your views here.

def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count() # the a stands for available
    num_authors = Author.objects.all().count()
    num_genres = Genre.objects.all().count()
    num_book_containing = Book.objects.filter(title__icontains="the").count()
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'num_book_containing': num_book_containing,
    }
    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    context_object_name = "book_list"
    # queryset = Book.objects.filter(title__icontains = "the")[:5]
    def get_queryset(self):
        return Book.objects.filter(title__icontains = "the")[:5]
    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['school'] = "Futa"
        return context
    template_name = "/catalog/book_list.html"


# def booklist(request):
#     books = Book.object.all()
#     for book in books:
#         return book
    
#     context = {
#         'books': books
#     }
    
#     return render(request, context=context)

# class BookDetailView(generic.DetailView):
#     model = Book
    
def book_detail_view(request, primary_key):
    try:
        book = Book.objects.get(pk=primary_key)
    except Book.DoesNotExist:
        raise Http404('Book does not exist')

    return render(request, 'catalog/book_detail.html', context={'book': book})