# IS_2025-2
Notas de la clase de laboratorio de ingenieria de software.

# Clase 1 18/02/2025

## Antes de empezar

### ¿Qué es Django?
Es un framework de desarrollo web de código abierto, escrito en Python, que sigue el patrón de diseño Modelo-Vista-Template (MVT).

#### Ventajas
- facilidad de uso
- permite crear algo desde 0 a algo usable en poco tiempo (MVP,Minimum Viable Product)

#### Algunos Ejemplos
almenos en sus primeras versiones:

- Instagram
- Spotify

Para empezar debemos entender que so los entornos virtuales y como instalarlos. Ya que nos ayudan a tener paquetes con versiones especificas para cada proyecto.

## Entornos Virtuales
### ¿Qué es un entorno virtual en Python y por qué usarlo en Django?
Un entorno virtual en Python es un espacio aislado donde puedes instalar paquetes y librerías sin afectar el sistema global. Es especialmente útil cuando trabajas en diferentes proyectos, ya que cada uno puede requerir distintas versiones de las mismas dependencias.

#### ¿Por qué usar entornos virtuales en Django?
Cuando trabajas con Django, podrías tener múltiples proyectos en tu computadora. Algunos podrían usar Django 3.x, mientras que otros requieren Django 4.x. Si instalas Django globalmente, podrías enfrentar conflictos de versiones.

##### Ventajas de usar un entorno virtual: 

- Evita conflictos de versiones entre proyectos.
- Permite probar diferentes versiones de Django sin afectar otros proyectos.
- Mantiene el sistema limpio sin instalar paquetes globalmente.
- Hace que el proyecto sea más portátil y fácil de compartir con otros desarrolladores.

Para crear un entorno virtual en python se utiliza el siguiente comando:

```bash
python -m venv path/nombre_del_entorno
```
### buenas practicas
- crear un archivo `.gitignore` para ignorar los archivos de entorno virtual
- crear un archivo `requirements.txt` para guardar las dependencias del proyecto
- el nombre del entorno virtual debe ser `.venv`
- el entorno virtual debe estar en la carpeta raiz del proyecto

### Activar entorno virtual
En Mac y Linux
```bash
source .venv/bin/activate
```
En Windows
```bash
.venv\Scripts\activate
```
Una vez activado el entorno virtual, el nombre del entorno virtual aparecerá en la terminal.

```bash
(env) usuario@mi-computadora:~/mi_proyecto$
```

### desactivar entorno virtual
En Mac, Linux y Windows
```bash
deactivate
```

Ya teniendo el entorno virtual activado, podemos instalar las dependencias del proyecto (una de esas es Django).



## Instalación de Django

Una vez que tenemos el entorno virtual activado, podemos instalar Django en su ultima version con el siguiente comando:

```bash
pip install django
```

Si queremos instalar una version especifica de Django, podemos hacerlo con el siguiente comando:

```bash
pip install django==x.y.z
```
Siendo x.y.z la version que queremos instalar.

Para verificar la instalacion de django usamos el comando.

```bash
django-admin --version
```
Para cualquier duda sobre los comandos de Django, podemos utilizar el siguiente comando:

```bash
django-admin --help
```

## Crear un proyecto en Django

Para crear un proyecto en Django se utiliza el siguiente comando:

```bash
django-admin startproject <nombre_del_proyecto>
```

El nombre del proyecto no debe tener espacios ni `-` si se quiere un nombre compuesto, se puede utilizar guion bajo `_`.

### Estructura de un proyecto en Django

La estructuras del proyecto es la siguiente.

```bash
mi_proyecto/
│── manage.py
│── mi_proyecto/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   ├── wsgi.py
```

- `manage.py`: es un script que ayuda con la administración del proyecto. Con él se pueden crear aplicaciones, crear un servidor de desarrollo, entre otras cosas.
- `nombre_del_proyecto/`: es la carpeta que contiene el proyecto.
  - `__init__.py`: es un archivo que indica que la carpeta es un paquete de Python.
  - `settings.py`: es el archivo de configuración del proyecto. `-Importante`
  - `urls.py`: es el archivo que contiene las urls del proyecto. `-Importante`
  - `wsgi.py`: es el archivo que contiene la configuración para desplegar el proyecto en producción.
  - `asgi.py`: es el archivo que contiene la configuración para desplegar el proyecto en producción con ASGI.

## Correr el servidor

Para correr el servidor de desarrollo de Django se utiliza el siguiente comando (debe estar en la carpeta del proyecto a la altura de `manage.py`):

```bash
python manage.py runserver
```
si tienes dudas sobre los comandos de `manage.py` puedes utilizar el siguiente comando:

```bash
python manage.py --help
```

## Entendiendo la arquitectura MVT

- Modelo: es la representación de los datos que maneja el proyecto.
- Vista: es la logica de datos que maneja el proyecto.
- Template: es la representación visual de los datos que maneja el proyecto.

## Crear una aplicación en Django
A la altura de `manage.py` se utiliza el siguiente comando para crear una aplicación en Django:

```bash
python manage.py startapp <nombre_de_la_aplicacion>
```

### Estructura de una aplicación en Django

- `migrations/`: es la carpeta que contiene las migraciones de la aplicación.
- `__init__.py`: es un archivo que indica que la carpeta es un paquete de Python.
- `admin.py`: es el archivo de configuración del administrador de Django.
- `apps.py`: es el archivo de configuración de la aplicación.
- `models.py`: es el archivo que contiene los modelos de la aplicación.
- `tests.py`: es el archivo que contiene las pruebas de la aplicación.
- `views.py`: es el archivo que contiene las vistas de la aplicación.

### trabajar con la aplicacion en Django

Para trabajar con la aplicación en Django, debemos agregarla en el archivo `settings.py` en la variable `INSTALLED_APPS`.

```python  
INSTALLED_APPS = [
    ...
    'nombre_de_la_aplicacion',
    ...
]
```

## Implementación de Login y Registro en Django

### Configuración del sistema de autenticación

Django ya tiene un modelo de usuario (```django.contrib.auth.models.User```).

Ejecuta las migraciones iniciales para crear las tablas de autenticación en la base de datos:

``` bash
python manage.py migrate
```

Ahora, crea un superusuario para acceder al panel de administración:

```bash
python manage.py createsuperuser
```

Ingresa un nombre de usuario, correo y contraseña.

Ejecuta el servidor:

```bash
python manage.py runserver

```
Accede al panel en http://127.0.0.1:8000/admin/ e inicia sesión con el superusuario.

### Crear vistas de login y logout

Dentro de la app ```usuarios/```, edita ```views.py``` para manejar el login.

```python
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Usuario o contraseña incorrectos")
    
    return render(request, 'usuarios/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    return render(request, 'usuarios/dashboard.html')
```

### Configurar las URLs
Edita ```usuarios/urls.py```:

``` python
from django.urls import path
from .views import login_view, logout_view, dashboard

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
     path('dashboard/', dashboard, name='dashboard'),
]
```
Ahora, edita ```mi_proyecto/urls.py``` para incluir las rutas de autenticación:

### Crear una template en con el formulario de Login.

Para crear una template en Django, debemos crear una carpeta llamada `templates` en la raiz de la aplicación y dentro de ella crear una carpeta con el nombre de la aplicación y dentro de esa carpeta crear el archivo `nombre_de_la_vista.html`.

En nuestro caso la ruta seria. `usuarios/templates/usuarios/login.html` :

y el contenido de `login.html` sera:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <h2>Iniciar Sesión</h2>
    {% if messages %}
        {% for message in messages %}
            <p style="color: red;">{{ message }}</p>
        {% endfor %}
    {% endif %}
    <form method="post">
        {% csrf_token %}
        <label>Usuario:</label>
        <input type="text" name="username">
        <br>
        <label>Contraseña:</label>
        <input type="password" name="password">
        <br>
        <button type="submit">Ingresar</button>
    </form>
</body>
</html>
```
Y tambien  `usuarios/templates/usuarios/dashboard.html` el contenido de `dashboard.html` sera:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Dashboard</title>
</head>
<body>
    <h1>Bienvenido al Dashboard</h1>
    <p>Hola, {{ user.username }}. Has iniciado sesión correctamente.</p>
    <a href="{% url 'logout' %}">Cerrar sesión</a>
</body>
</html>

```


#### Codigo python en template

Para agregar codigo python en una template de Django, se utiliza la siguiente sintaxis:

```html
{% codigo_python %}
```
siempre se debe cerrar el bloque de codigo python con la siguiente sintaxis:

```html
{% endcodigo_python %}
```
Algunos ejemplos Basicos de codigo python en template:

```html
{% if condicion %}
    ...
{% endif %}

{% for item in lista %}
    ...
{% endfor %}

{% block nombre_del_bloque %}
    ...
{% endblock %}
```

