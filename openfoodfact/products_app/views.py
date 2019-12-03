from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import models
from django.template import Context, Template
from products_app import search


def home(request):
    return render(request, 'products_app/home.html')


def search_products(request):
    message = None
    query = request.GET.get('query')
    if not query:
        message = "Votre saisie est vide !"
    else:
        product = Products.objects.filter(name__icontains=query)  # Insensible a la casse
        print(product)
        search_products()
    if not product.exists():
        message = "Votre produit n'existe pas dans notre base de donnée !"


    context = {
        'product': product,
        'alternativ_products': list,
        'message_to_display': message
    }
    return render(request, 'result.html', context)


def product_page(request):
    return render(request, 'product_page.html')


def create_user(request):
    user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')


def authenticate(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
        ...

def logout_view(request):
    logout(request)
    # Redirect to a success page.