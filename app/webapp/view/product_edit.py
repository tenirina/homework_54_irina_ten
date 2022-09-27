from django.shortcuts import get_object_or_404, render, redirect

from webapp.models.category import Category
from webapp.models.product import Product


def product_edit_view(request, pk):
    if request.method == "GET":
        product = get_object_or_404(Product, pk=pk)
        context = {
            'choices': Category.objects.all(),
            'product': product
        }
        return render(request, 'product_edit.html', context=context)
    product_data = {
        'name': request.POST.get("text"),
        'price': request.POST.get("price"),
        'picture': request.POST.get("png"),
        'category': Category.objects.get(name=request.POST.get("category")),
        'description': request.POST.get("textarea"),
    }
    product = get_object_or_404(Product, pk=pk)
    product.name = product_data['name']
    product.price = product_data['price']
    product.picture = product_data['picture']
    product.category = product_data['category']
    product.description = product_data['description']
    product.save()
    return redirect('product', pk=product.pk)
