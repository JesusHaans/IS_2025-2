import pytest
from django.urls import reverse
from datetime import date
from books.models import Book, Publisher, Category

# -------------------------------
# Pruebas para la vista de listado
# -------------------------------

@pytest.mark.django_db
def test_book_list_redirects_for_anonymous(client):
    """
    Verifica que un usuario no autenticado sea redirigido al intentar acceder a la lista de libros.
    """
    url = reverse('books:book_list')
    response = client.get(url)
    # Debería redirigir al login (código 302) y la URL de redirección debe contener "login"
    assert response.status_code == 302
    assert '/accounts/login/' in response.url or 'login' in response.url

@pytest.mark.django_db
def test_book_list_for_authenticated(client, django_user_model):
    """
    Verifica que un usuario autenticado pueda acceder a la lista de libros.
    """
    username = "testuser"
    password = "testpass"
    django_user_model.objects.create_user(username=username, password=password)
    client.login(username=username, password=password)
    
    url = reverse('books:book_list')
    response = client.get(url)
    assert response.status_code == 200
    # Se verifica que el template contenga un título esperado (por ejemplo, "Lista de Libros")
    assert "Lista de Libros" in response.content.decode()

# -------------------------------------------
# Función auxiliar para crear datos de prueba
# -------------------------------------------

@pytest.mark.django_db
def create_test_data():
    """
    Crea una editorial, dos categorías y un libro asociado a esas instancias.
    Retorna el objeto Book creado para usarlo en otras pruebas.
    """
    publisher = Publisher.objects.create(name="Test Publisher")
    cat1 = Category.objects.create(name="Categoría 1")
    cat2 = Category.objects.create(name="Categoría 2")
    book = Book.objects.create(
        title="Libro de Prueba",
        author="Autor de Prueba",
        publication_date=date(2022, 1, 1),
        isbn="1234567890123",
        summary="Resumen de prueba",
        publisher=publisher,
    )
    book.categories.set([cat1, cat2])
    return book

# -------------------------------
# Pruebas para la vista de detalle
# -------------------------------

@pytest.mark.django_db
def test_book_detail_for_authenticated(client, django_user_model):
    """
    Verifica que un usuario autenticado pueda acceder al detalle de un libro.
    """
    book = create_test_data()
    username = "testuser"
    password = "testpass"
    django_user_model.objects.create_user(username=username, password=password)
    client.login(username=username, password=password)
    
    url = reverse('books:book_detail', kwargs={'pk': book.pk})
    response = client.get(url)
    assert response.status_code == 200
    # El contenido de la página debe incluir el título del libro
    assert book.title in response.content.decode()

# ---------------------------------
# Prueba para la creación de un libro
# ---------------------------------

@pytest.mark.django_db
def test_create_book_view(client, django_user_model):
    """
    Verifica que un usuario autenticado pueda crear un nuevo libro mediante la vista de creación.
    """
    username = "testuser"
    password = "testpass"
    django_user_model.objects.create_user(username=username, password=password)
    client.login(username=username, password=password)
    
    # Crear una editorial y algunas categorías para asignarlas al libro
    publisher = Publisher.objects.create(name="Editorial de Prueba")
    cat1 = Category.objects.create(name="Categoría A")
    cat2 = Category.objects.create(name="Categoría B")
    
    url = reverse('books:book_create')
    data = {
        'title': 'Nuevo Libro',
        'author': 'Nuevo Autor',
        'publication_date': '2023-01-01',
        'isbn': '9876543210123',
        'summary': 'Resumen del nuevo libro',
        'publisher': publisher.id,
        'categories': [cat1.id, cat2.id],
    }
    response = client.post(url, data)
    
    # Se espera una redirección tras la creación (código 302)
    assert response.status_code == 302
    assert Book.objects.filter(title='Nuevo Libro').exists()

# -------------------------------
# Prueba para la edición de un libro
# -------------------------------

@pytest.mark.django_db
def test_update_book_view(client, django_user_model):
    """
    Verifica que un usuario autenticado pueda actualizar los datos de un libro.
    """
    book = create_test_data()
    username = "testuser"
    password = "testpass"
    django_user_model.objects.create_user(username=username, password=password)
    client.login(username=username, password=password)

    url = reverse('books:book_update', kwargs={'pk': book.pk})
    data = {
        'title': 'Libro Actualizado',
        'author': book.author,
        'publication_date': book.publication_date,
        'isbn': book.isbn,
        'summary': book.summary,
        'publisher': book.publisher.id,
        'categories': [cat.pk for cat in book.categories.all()],
    }
    response = client.post(url, data)
    assert response.status_code == 302
    book.refresh_from_db()
    assert book.title == 'Libro Actualizado'

# -------------------------------
# Prueba para la eliminación de un libro
# -------------------------------

@pytest.mark.django_db
def test_delete_book_view(client, django_user_model):
    """
    Verifica que un usuario autenticado pueda eliminar un libro.
    """
    book = create_test_data()
    username = "testuser"
    password = "testpass"
    django_user_model.objects.create_user(username=username, password=password)
    client.login(username=username, password=password)

    url = reverse('books:book_delete', kwargs={'pk': book.pk})
    response = client.post(url)
    assert response.status_code == 302
    # Confirmar que el libro ya no existe en la base de datos
    assert not Book.objects.filter(pk=book.pk).exists()