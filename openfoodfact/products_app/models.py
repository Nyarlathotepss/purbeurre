from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    ingredient = models.TextField(max_length=300, null=True)
    nutriscore = models.CharField(max_length=1, null=False)
    store = models.CharField(max_length=30, null=True)
    url = models.URLField(max_length=300, null=False)
    id_category = models.ForeignKey(Category, on_delete=models.CASCADE)


class User(models.Model):
    user_id = models.IntegerField(max_length=1000,null=False)
    password = models.CharField(max_length=30, null=False)
    email = models.EmailField(max_length=70)