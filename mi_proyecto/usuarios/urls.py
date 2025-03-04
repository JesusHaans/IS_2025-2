from django.urls import path
from .views import login_view, logout_view, dashboard, inicio_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('inicio/', inicio_view, name ='inicio'),
]
