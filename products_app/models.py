from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    ingredient = models.TextField(max_length=300, null=True)
    nutriscore = models.CharField(max_length=1, null=False)
    store = models.CharField(max_length=200, null=True)
    url = models.URLField(max_length=300, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image_url = models.URLField(max_length=500, null=False)
    fat_100g = models.CharField(max_length=8, null=True)
    saturated_fat_100g = models.CharField(max_length=8, null=True)
    salt_100g = models.CharField(max_length=8, null=True)
    sugars_100g = models.CharField(max_length=8, null=True)
    favorite_of = models.ManyToManyField(User)

    def __str__(self):
        return self.category, self.name
