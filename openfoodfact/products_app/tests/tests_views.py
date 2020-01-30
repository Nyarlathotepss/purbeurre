from django.test import TestCase
from django.test import Client
from products_app.models import *


class ProductAppTest(TestCase):

    def setUp(self):
        self.julien = User.objects.create_user("julien, julien@test.fr, password")
        self.clara = User.objects.create_user("clara, clara@test.fr, password")
        self.medhi = User.objects.create_user("medhi, medhi@test.fr, password")

    def test_home_view(self):
        response = self.client.get('/home/')
        self.assertEqual(response.status_code, 200)

    def test_home_authenticated_user(self):
        self.client.login(username="julien", password="password")
        response = self.client.get('/home/')
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        # Check that the rendered context contains 1 customer.
        self.assertEqual(len(response.context['customers']), 1)

    def test_home_unauthenticated_user(self):
        self.client.login(username="julien", password="password")
        self.client.logout()
        response = self.client.get('/home/')
        self.assertEqual(response.status_code, 200)

    def test_search_product_view(self):
        response = self.client.get('/result/')
        self.assertEqual(response.status_code, 200)

    def test_search_product_page(self):
        response = self.client.get('/product_page/')
        self.assertEqual(response.status_code, 200)

    def test_user_connection(self):
        c = Client()
        response = c.get('/login/')
        self.assertEqual(response.status_code, 200)
        self.client.login(username="clara", password="password")
        response = self.client.get('/home/')
        self.assertEqual(response.status_code, 200)





