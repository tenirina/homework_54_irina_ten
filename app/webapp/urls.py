from django.urls import path


from webapp.view.base import products_view
from webapp.view.categories import categories_view
from webapp.view.category_add import category_add_view
from webapp.view.product import product_view

urlpatterns = [
    path("", products_view, name="products"),
    path("products/", products_view, name="products"),
    path("products/<int:pk>", product_view, name="product"),
    path("categories/add/", category_add_view, name="category_add"),
    path("categories/", categories_view, name="categories"),
]
