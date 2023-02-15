from django.urls import path
from .views import *

urlpatterns = [
    path("", homepage, name="homepage"),
    path("add-product/", add_product, name="add_product"),
    path("edit-product-<int:product_id>/", edit_product, name="edit_product"),
    path("delete-product-<int:product_id>/",
         delete_product, name="delete_product"),
]