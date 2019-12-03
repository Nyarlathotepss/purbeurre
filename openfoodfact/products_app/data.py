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
                if json['products'][k]['product_name'].lower().strip() in list_names_products:
                    k += 1
                    continue
                else:
                    self.info_products.append((json['products'][k]['product_name'],
                                               json['products'][k]['ingredients_text_fr'],
                                               json['products'][k]['nutrition_grade_fr'],
                                               json['products'][k]['purchase_places'],
                                               json['products'][k]['url'],
                                               json['products'][k]['image_url']))
                    list_names_products.append(self.info_products[-1][0].lower().strip())
                    k += 1
            except KeyError:
                k += 1
                continue

    def insert_data_category_into_bdd(self):
        for category in constant.LIST_CATEGORIES:
            data = Category(name=category)
            data.save()

    def insert_data_product_into_bdd(self, id_category):
        for product in self.info_products:
            print(product)
            try:
                data = Product(name=product[0], ingredient=product[1],
                               nutriscore=product[2], store=product[3],
                               url=product[4], category_id=id_category, image_url=product[5])
                data.save()
            except Exception as e:
                print(e)
