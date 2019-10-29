from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class User(models.Model):
    user_id = models.IntegerField(null=False)
    password = models.CharField(max_length=30, null=False)
    email = models.EmailField(max_length=70)

    def __str__(self):
        return self.user_id


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    ingredient = models.TextField(max_length=300, null=True)
    nutriscore = models.CharField(max_length=1, null=False)
    store = models.CharField(max_length=200, null=True)
    url = models.URLField(max_length=300, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    favorite = models.ManyToManyField(User, related_name='favorites', blank=True)

    def __str__(self):
        return self.name
