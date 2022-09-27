from django.shortcuts import render

from webapp.models.category import Category


def categories_view(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', context={'categories': categories})
