from django.db import models

# Create your models here.

# Modelo para Editorial (relación Uno a Muchos con Book)
class Publisher(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre de la Editorial")
    website = models.URLField(blank=True, null=True, verbose_name="Sitio Web")

    def __str__(self):
        return self.name

# Modelo para Categoría (relación Muchos a Muchos con Book)
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Categoría")

    def __str__(self):
        return self.name

# Modelo principal Libro
class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    author = models.CharField(max_length=100, verbose_name="Autor")
    publication_date = models.DateField(verbose_name="Fecha de Publicación")
    isbn = models.CharField(max_length=13, unique=True, verbose_name="ISBN")
    summary = models.TextField(blank=True, verbose_name="Resumen")
    
    # Relación Uno a Muchos: Cada libro pertenece a una Editorial.
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.CASCADE,
        related_name='books',
        verbose_name="Editorial"
    )
    
    # Relación Muchos a Muchos: Un libro puede pertenecer a múltiples Categorías.
    categories = models.ManyToManyField(
        Category,
        blank=True,
        related_name='books',
        verbose_name="Categorías"
    )

    def __str__(self):
        return self.title

# Modelo para Detalle del Libro (relación Uno a Uno con Book)
class BookDetail(models.Model):
    # Cada registro de detalle se relaciona de forma exclusiva a un libro.
    book = models.OneToOneField(
        Book,
        on_delete=models.CASCADE,
        related_name='detail',
        verbose_name="Libro"
    )
    number_of_pages = models.PositiveIntegerField(verbose_name="Número de Páginas")
    language = models.CharField(max_length=50, verbose_name="Idioma")
    # Requiere configuración previa para el manejo de imágenes (opcional)
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True, verbose_name="Imagen de Portada")

    def __str__(self):
        return f"Detalles de {self.book.title}"