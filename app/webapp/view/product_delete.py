from django.shortcuts import get_object_or_404, redirect

from webapp.models.product import Product


def product_delete_view(request, pk):
    category = get_object_or_404(Product, pk=pk)
    category.delete()
    return redirect('products')
