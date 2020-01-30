from django.test import TestCase
from products_app.models import Product, Category, Favorite


class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Category.objects.create(name='fruits et légumes')

    def test_name_label(self):
        product = Product.objects.get(pk='1')
        field_label = product.__meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')


class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Product.objects.create(name='jus de goyave', nutriscore='c', url='http://goyave.fr', category='boissons',
                               image_url='http://lechemindelimage')

    def test_name_label(self):
        product = Product.objects.get(pk='1')
        field_label = product.__meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_category_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('ingredient').verbose_name
        self.assertEquals(field_label, 'ingredient')

    def test_name_max_lenght(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)

    def test_object_name_is_category_comma_name(self):
        product = Product.objects.get(id=1)
        expected_object_name = f'{product.category}, {product.name}'
        self.assertEquals(expected_object_name, str(product))

