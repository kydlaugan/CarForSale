from django.urls import path 

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('liste/', views.liste, name='liste'),
    path('liste/details/<int:id>/', views.details, name='details'),
    path('creation/<int:id>/', views.creer_voiture, name='creation'),
    path('connexion/dashboard/<int:id>/', views.dashboard, name='dashboard'),
    path('connexion/', views.connexion, name='connexion'),
    path('register/', views.register, name='register'),
    path('connexion/dashboard/delete/<int:id>', views.delete_voiture, name = 'delete'),
    path('modifier/<int:id>', views.a_jour_voiture, name = 'modifier'),
    path('liste/recherche', views.recherche, name = 'recherche'),



]