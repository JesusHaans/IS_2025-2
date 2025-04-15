from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Book

# Aplicamos el login_required a cada vista basada en clase usando method_decorator.

@method_decorator(login_required, name='dispatch')
class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'

@method_decorator(login_required, name='dispatch')
class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'

@method_decorator(login_required, name='dispatch')
class BookCreateView(CreateView):
    model = Book
    template_name = 'books/book_form.html'
    fields = ['title', 'author', 'publication_date', 'isbn', 'summary', 'publisher', 'categories']
    success_url = reverse_lazy('books:book_list')

@method_decorator(login_required, name='dispatch')
class BookUpdateView(UpdateView):
    model = Book
    template_name = 'books/book_form.html'
    fields = ['title', 'author', 'publication_date', 'isbn', 'summary', 'publisher', 'categories']
    success_url = reverse_lazy('books:book_list')

@method_decorator(login_required, name='dispatch')
class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/book_confirm_delete.html'
    success_url = reverse_lazy('books:book_list')