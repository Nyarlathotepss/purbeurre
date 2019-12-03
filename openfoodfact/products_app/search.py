from products_app.models import Product
import random


class Search:

    def search_products(self, category, product_get):
        q1 = Product.objects.filter(category=category)
        q2 = q1.exclude(name=product_get)
        all_entries = q2.all()
