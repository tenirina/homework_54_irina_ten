from django.shortcuts import redirect, render

from webapp.models.category import Category


def category_add_view(request):
    if request.method == "GET":
        return render(request, 'category_add.html')
    category_data = {
        'name': request.POST.get('text'),
        'description': request.POST.get('textarea')
    }
    category = Category.objects.create(**category_data)
    return redirect('category', pk=category.pk)
