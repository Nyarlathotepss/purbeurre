from django.test import TestCase
from django.test import Client
from products_app.models import Product

c = Client()
response = c.post('/login/', {'username': 'john', 'password': 'smith'})
