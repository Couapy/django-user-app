from django.urls import path

from . import views

app_name = "account"
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name="register"),
    path('profile/', views.profile, name='profile'),
    path('user/', views.user, name='user'),
    path('password/', views.password, name='password'),
    path('connections/', views.connections, name='connections'),
    path('delete/', views.delete, name='delete'),
]
