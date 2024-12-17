from django.urls import path
from PapiroBooks_app import views

urlpatterns = [
    path('', views.home, name='home'), #página inicial
    path('generos/', views.generos, name='generos'), #página gêneros
    path('info_livro/hipotese/', views.info_livro_hipotese, name='info_livro_hipotese'),#página livro hipótese
    path('info_livro/amor/', views.info_livro_amor, name='info_livro_amor'), #página livro amor
    path('biblioteca/', views.biblioteca, name='biblioteca'), #página biblioteca
    path('amigos/', views.amigos, name='amigos'), #página amigos
    path('navbar/', views.navbar, name='navbar'),
]

