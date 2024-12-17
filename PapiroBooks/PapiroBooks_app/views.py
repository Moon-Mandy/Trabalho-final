from django.shortcuts import render, redirect

def home(request):
    return render(request, "home.html")

def generos(request):
    return render(request, "generos.html")

def info_livro_hipotese(request):
    return render(request, "info_livro_hipotese.html")

def info_livro_amor(request):
    return render(request, "info_livro_amor.html")

def biblioteca(request):
    return render(request, "biblioteca.html")

def amigos(request):
    return render(request, "amigos.html")

def navbar(request):
    return render(request,"navbar.html")

