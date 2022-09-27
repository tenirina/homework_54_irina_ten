from django.urls import path


from webapp.view.base import products_view
from webapp.view.categories import categories_view
from webapp.view.category import category_view
from webapp.view.category_add import category_add_view
from webapp.view.category_delete import category_delete_view
from webapp.view.category_edit import category_edit_view
from webapp.view.product import product_view
from webapp.view.product_add import product_add_view
from webapp.view.product_delete import product_delete_view
from webapp.view.product_edit import product_edit_view

urlpatterns = [
    path("", products_view, name="products"),
    path("products/", products_view, name="products"),
    path("products/add/", product_add_view, name="products_add"),
    path("products/<int:pk>", product_view, name="product"),
    path("categories/add/", category_add_view, name="category_add"),
    path("categories/", categories_view, name="categories"),
    path("categories/<int:pk>", category_view, name="category"),
    path("categories/<int:pk>/edit", category_edit_view, name="category_edit"),
    path("categories/<int:pk>/delete", category_delete_view, name="category_delete"),
    path("products/<int:pk>/delete", product_delete_view, name="product_delete"),
    path("products/<int:pk>/edit", product_edit_view, name="product_edit")
]
