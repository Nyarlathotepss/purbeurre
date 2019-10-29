from products_app import api, constant
from products_app.models import Product, Category


class Data:
    def __init__(self):
        self.info_products = []

    def get_info_from_json(self, json):
        k = 0
        list_names_products = []
        while k < constant.LIMIT_PRODUCTS:
            try:
                self.info_products = (json['products'][k]['product_name'],
                                      json['products'][k]['ingredients_text_fr'],
                                      json['products'][k]['nutrition_grade_fr'],
                                      json['products'][k]['purchase_places'],
                                      json['products'][k]['url'])
                if self.info_products[0].lower().strip() in list_names_products:
                    k += 1
                    continue
                else:
                    list_names_products.append(self.info_products[0].lower().strip())
            except KeyError:
                k += 1
                continue

    def insert_data_category_into_bdd(self):
        for category in constant.LIST_CATEGORIES:
            data = Category(name=category)
            data.save()

    def insert_data_product_into_bdd(self, id_category):
        for product in enumerate(self.info_products):
            data = Product(name=product[0], ingredient=product[1],
                           nutriscore=self.info_products[2], store=self.info_products[3],
                           url=self.info_products[4], category_id=id_category)
            data.save()
