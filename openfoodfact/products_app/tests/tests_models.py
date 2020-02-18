from django.test import TestCase
from products_app.models import Product, Category


class ModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        category = Category.objects.create(id=1, name='fruits et légumes')
        category.save()
        product = Product.objects.create(id=1, name='papaye', nutriscore='c', url='http://papaye.fr', category=category,
                                         image_url='http://lechemindelimage', fat_100g='0', saturated_fat_100g='0',
                                         salt_100g='0', sugars_100g='10', ingredient=None)
        product.save()

    def test_product_ingredient_label(self):
        """ Check the label name"""
        category = Category.objects.get(pk='1')
        field_label = category._meta.get_field('ingredient').verbose_name
        self.assertEquals(field_label, 'ingredient')

    def test_category_name_label(self):
        """ Check the label name"""
        category = Category.objects.get(pk='1')
        field_label = category._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_category_name_max_lenght(self):
        """ Check the max length """
        category = Category.objects.get(pk='1')
        max_length = category._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)

    def test_product_name_label(self):
        product = Product.objects.get(pk='1')
        field_label = product._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_product_name_max_lenght(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)

    def test_product_nutriscore_label(self):
        product = Product.objects.get(pk='1')
        field_label = product._meta.get_field('nutriscore').verbose_name
        self.assertEquals(field_label, 'nutriscore')

    def test_product_nutriscore_max_lenght(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('nutriscore').max_length
        self.assertEquals(max_length, 1)

    def test_product_url_label(self):
        product = Product.objects.get(pk='1')
        field_label = product._meta.get_field('url').verbose_name
        self.assertEquals(field_label, 'url')

    def test_product_url_max_lenght(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('url').max_length
        self.assertEquals(max_length, 300)

    def test_product_category_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('category').verbose_name
        self.assertEquals(field_label, 'category')

    def test_product_image_url_max_length(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('image_url').max_length
        self.assertEquals(max_length, 500)

    def test_product_image_url_label(self):
        product = Product.objects.get(pk='1')
        field_label = product._meta.get_field('image_url').verbose_name
        self.assertEquals(field_label, 'image url')

    def test_product_fat_100g_label(self):
        product = Product.objects.get(pk='1')
        field_label = product._meta.get_field('fat_100g').verbose_name
        self.assertEquals(field_label, 'fat 100g')

    def test_product_fat_100g_max_length(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('fat_100g').max_length
        self.assertEquals(max_length, 8)

    def test_product_saturated_fat_100g_max_length(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('saturated_fat_100g').max_length
        self.assertEquals(max_length, 8)

    def test_product_saturated_fat_100g_label(self):
        product = Product.objects.get(pk='1')
        field_label = product._meta.get_field('saturated_fat_100g').verbose_name
        self.assertEquals(field_label, 'saturated fat 100g')

    def test_product_salt_100g_max_length(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('salt_100g').max_length
        self.assertEquals(max_length, 8)

    def test_product_salt_100g_label(self):
        product = Product.objects.get(pk='1')
        field_label = product._meta.get_field('salt_100g').verbose_name
        self.assertEquals(field_label, 'salt 100g')

    def test_product_sugars_100g_max_length(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('sugars_100g').max_length
        self.assertEquals(max_length, 8)

    def test_product_sugars_100g_label(self):
        product = Product.objects.get(pk='1')
        field_label = product._meta.get_field('sugars_100g').verbose_name
        self.assertEquals(field_label, 'sugars 100g')

    def test_product_object_name_is_category_comma_name(self):
        product = Product.objects.get(id=1)
        expected_object_name = f'{product.category}, {product.name}'
        self.assertEquals(expected_object_name, 'fruits et légumes, papaye')


