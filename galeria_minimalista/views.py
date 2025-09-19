from django.shortcuts import render


def index(request):
    return render(request, "galeria_minimalista/index.html")
