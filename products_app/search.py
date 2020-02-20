from products_app.models import Product


class Search:
    """ Search in database """

    @staticmethod
    def search_products_better(category, name, nutriscore):
        """ Search [1-6] product with a better nutriscore """
        query = Product.objects.filter(category=category)
        if nutriscore == "a":
            data = query.filter(nutriscore__exact=nutriscore)
            data = data.exclude(name=name)
            queryset = data[:6]
        else:
            data = query.filter(nutriscore__lt=nutriscore)
            data = data.exclude(name=name)
            queryset = data[:6]
        return queryset

    @staticmethod
    def search_product_by_id(product_id):
        """ Search a product with his unique ID """
        query = Product.objects.filter(pk=product_id)
        return query
