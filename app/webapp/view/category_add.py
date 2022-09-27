from django.shortcuts import redirect, render

from webapp.models import Category


def category_add_view(request):
    category_data = {
        'name': request.POST.get('text'),
        'description': request.POST.get('textarea')
    }
    category = Category.objects.create(**category_data)
    print(category)
    print(category_data)
    return render(request, 'category_add.html', context={'category': category})
