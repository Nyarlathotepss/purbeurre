from django.conf import settings
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^result/', views.search_products, name="result"),
    url(r'product_number/([0-9]{1,8})/', views.product_page, name="product_page"),
    url('product_save/', views.product_save, name="product_save"),
    url(r'favorites/', views.favorites, name="favorites")
]