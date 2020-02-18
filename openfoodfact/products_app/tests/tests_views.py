from django.test import TestCase
from django.test import Client
from products_app.models import *


class ProductAppTest(TestCase):

    def setUp(self):
        self.julien = User.objects.create_user("julien, julien@test.fr, password")

    def test_home_view(self):
        response = self.client.get('/')
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    def test_result_view(self):
        response = self.client.get('/products_app/result/')
        self.assertEqual(response.status_code, 200)

    def test_product_page_view(self):
        response = self.client.get('/products_app/product_number/1630/')
        self.assertEqual(response.status_code, 200)

    def test_product_saved_authenticated_user_view(self):
        self.client.login(username="julien", password="password")
        response = self.client.get('/products_app/product_save/')
        self.assertEqual(response.status_code, 200)

    def test_product_saved_unauthenticated_user_view(self):
        response = self.client.get('/products_app/product_save/')
        self.assertEqual(response.status_code, 302)

    def test_home_authenticated_user(self):
        self.client.login(username="julien", password="password")
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_unauthenticated_user(self):
        self.client.login(username="julien", password="password")
        self.client.logout()
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_user_account_authenticated_user(self):
        self.client.login(username="julien", password="password")
        response = self.client.get('accounts/user_account/')
        self.assertEqual(response.status_code, 200)

    def test_user_account_unauthenticated_user(self):
        self.client.login(username="julien", password="password")
        self.client.logout()
        response = self.client.get('/accounts/user_account/')
        self.assertEqual(response.status_code, 302)

    def test_login(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        self.client.login(username="julien", password="password")
        self.client.logout()
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_signup(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_favorites(self):
        self.client.login(username="julien", password="password")
        response = self.client.get('/products_app/favorites/')
        self.assertEqual(response.status_code, 200)

    def test_user_connection(self):
        c = Client()
        response = c.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)
        self.client.login(username="julien", password="password")
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)





