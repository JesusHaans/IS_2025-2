# Generated by Django 5.1.6 on 2025-04-08 01:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('author', models.CharField(max_length=100, verbose_name='Autor')),
                ('publication_date', models.DateField(verbose_name='Fecha de Publicación')),
                ('isbn', models.CharField(max_length=13, unique=True, verbose_name='ISBN')),
                ('summary', models.TextField(blank=True, verbose_name='Resumen')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Categoría')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre de la Editorial')),
                ('website', models.URLField(blank=True, null=True, verbose_name='Sitio Web')),
            ],
        ),
        migrations.CreateModel(
            name='BookDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_pages', models.PositiveIntegerField(verbose_name='Número de Páginas')),
                ('language', models.CharField(max_length=50, verbose_name='Idioma')),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='book_covers/', verbose_name='Imagen de Portada')),
                ('book', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='detail', to='books.book', verbose_name='Libro')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='books', to='books.category', verbose_name='Categorías'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='books.publisher', verbose_name='Editorial'),
        ),
    ]
