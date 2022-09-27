from django.shortcuts import render, get_object_or_404

from webapp.models.product import Product


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product.html', context={'product': product})
