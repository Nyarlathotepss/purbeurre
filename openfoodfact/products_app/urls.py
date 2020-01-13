from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^result/', views.search_products, name="result"),
    url(r'^product/', views.product_page, name="product_page")
]