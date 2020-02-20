from django.core.management.base import BaseCommand, CommandError
from products_app import data, constant, api
from products_app.models import Category


class Command(BaseCommand):
    help = 'The command : request api openfoodfact' \
           '              get informations from json' \
           '              insert this info in database'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        try:
            object_api = api.Api()
            object_data = data.Data()
            object_data.insert_data_category_into_bdd()  # insert categories names
            for category in constant.LIST_CATEGORIES:
                param = object_api.generate_parameters(category)  # api create parameter
                my_json = object_api.communication_api(constant.URL_OPENFOODFACT, param)  # api request
                object_data.get_info_from_json(my_json)  # get info from json
                p = Category.objects.get(name=category)  # get category id from bdd
                id_category = p.id
                object_data.insert_data_product_into_bdd(id_category)  # insert info product
        except Exception as e:
            raise CommandError(e)

