from django.shortcuts import get_object_or_404, redirect

from webapp.models.category import Category


def category_delete_view(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories')
