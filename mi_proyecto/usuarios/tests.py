from django.test import TestCase
from .models import Entrada
import pytest

# Create your tests here.
#@pytest.mark.xfail(reason="no funciona en windows")
@pytest.mark.django_db
def test_func():
    entrada = Entrada.objects.create(
        aidi='12367',
        nombre='Estudiante 1',
        fecha='2021-09-01'
    )
    assert entrada.aidi == '12367'

@pytest.mark.django_db
def test_entrada_nombre():
    entrada = Entrada.objects.create(
        aidi='12367',
        nombre='Estudiante 2',
        fecha='2021-09-01'
    )
    assert entrada.nombre == 'Estudiante 2'

# @pytest.mark.urls
# @pytest.mark.parametrize(cadena o lista de cadenas, lista iterable(lñista, tuplas, etc))
# @pytest.mark.skip(reason="funcionm no implementada")
# import sys
# @pytest.mark.skipif(sys.platform == "win32", reason="no funciona en windows")
# @pytest.mark.xfail(reason="no funciona en windows")
# REST framework
# @pytest.mark.asyncio