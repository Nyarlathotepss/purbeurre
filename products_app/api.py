import requests
from products_app import constant


class Api:
    """Communicate with API"""

    @staticmethod
    def communication_api(url, dict_parameters):
        """ got .json from api openfoodfact """
        request = requests.get(url, dict_parameters)
        return request.json()

    @staticmethod
    def generate_parameters(category):
        """ generate parameters of request """
        param_url = {'action': 'process',
                     'tagtype_0': 'categories',
                     'tag_contains_0': 'contains',
                     'tag_0': category,
                     'sort_by': 'unique_scans_n',
                     'page_size': constant.LIMIT_PRODUCTS,
                     'axis_x': 'energy',
                     'axis_y': 'products_n',
                     'json': '1'}
        return param_url
