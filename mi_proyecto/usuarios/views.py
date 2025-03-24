from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Entrada

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
    
    ## entradas_Hoy = [
    ##    {'id': '12367', 'nombre': 'Estudiante 1', 'fecha': '2021-09-01'},
    ##    {'id': '09865', 'nombre': 'Estudiante 2', 'fecha': '2021-09-02'},
    ##    {'id': '29384', 'nombre': 'Estudiante 3', 'fecha': '2021-12-01'},
    ##    {'id': '12367', 'nombre': 'haans', 'fecha': '2021-12-02'},
    ##    {'id': '09865', 'nombre': 'link', 'fecha': '2021-12-03'},
    ##]
    entradas_Hoy = Entrada.objects.all()

    contexto = {
        'entradas_Hoy': entradas_Hoy
    }
    return render(request, 'usuarios/dashboard.html', contexto)

def registro(request):
    if request.method == "POST":
        formulario = UserCreationForm(request.POST)
        print(request.POST)
        print(formulario)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Usuario creado exitosamente")
            return redirect('login')

    formulario = UserCreationForm()
    print(formulario)
    return render(request, 'usuarios/registro.html', {'formulario': formulario})

def nueva(request):
    return render(request, 'usuarios/nueva.html')