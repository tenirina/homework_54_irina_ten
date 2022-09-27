from django.shortcuts import render

from webapp.models import Category


def categories_view(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', context={'categories': categories})
