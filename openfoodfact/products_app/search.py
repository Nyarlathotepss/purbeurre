from products_app.models import Product


class Search:

    def search_products(self, product_category, product_name):
        q1 = Product.objects.filter(category=product_category)
        q2 = q1.exclude(name=product_name)
        all_entries = q2[0:6]
        return all_entries
