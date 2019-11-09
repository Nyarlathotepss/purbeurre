from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'products_app/home.html')


def result(request):
    return render(request, 'result.html')


def product(request):
    return render(request, 'product_page.html')
