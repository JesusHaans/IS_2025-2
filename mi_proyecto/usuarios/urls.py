from django.urls import path
from .views import login_view, logout_view, dashboard, nueva

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('nueva/', nueva,  name='nueva'),
]
