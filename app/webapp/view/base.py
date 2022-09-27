from django.shortcuts import render

from webapp.models.product import Product


def products_view(request):
    products = Product.objects.all()
    return render(request, 'products.html', context={'products': products})
