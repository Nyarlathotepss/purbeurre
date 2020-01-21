from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import models
from django.template import Context, Template
from products_app.models import Product
from products_app import search

nutri_list = ["a", "b", "c", "d", "e"]


def home(request):
    return render(request, 'products_app/home.html')


def search_products(request):
    product, message, substitute_products, context = None, None, None, None
    my_search = search.Search()
    query = request.GET.get('query')
    if not query:
        message = "Votre saisie est vide !"
    else:
        product = Product.objects.filter(name__icontains=query)  # Insensible a la casse

        if not product.exists():
            message = "Votre produit n'existe pas dans notre base de donnée !"
        else:
            product = product.all()[0]
            print(product)
            substitute_products = my_search.search_products(product.category, product.name)
            message = "Voici des produits de subsitution :"
    context = {
                'product': product,
                'alternativ_products': substitute_products,
                'message_to_display': message,
                'nutricode_list': nutri_list
              }
    return render(request, 'products_app/result.html', context)


def product_page(request):
    return render(request, 'product_page.html')