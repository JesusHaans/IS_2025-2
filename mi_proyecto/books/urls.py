from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

app_name = 'books'

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('nuevo/', BookCreateView.as_view(), name='book_create'),
    path('<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('<int:pk>/editar/', BookUpdateView.as_view(), name='book_update'),
    path('<int:pk>/eliminar/', BookDeleteView.as_view(), name='book_delete'),
]