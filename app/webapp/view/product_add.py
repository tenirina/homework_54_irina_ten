from django.shortcuts import render, redirect
from django.urls import reverse

from webapp.models import Product, Category


def product_add_view(request):
    if request.method == "GET":
        context = {
            'choices': Category.objects.all()
        }
        return render(request, 'product_add.html', context)
    product_data = {
        'name': request.POST.get("text"),
        'price': request.POST.get("price"),
        'picture': request.POST.get("png"),
        'category': Category.objects.get(name=request.POST.get("category")),
        'description': request.POST.get("textarea"),
    }
    product = Product.objects.create(**product_data)
    return redirect('product', pk=product.pk)
