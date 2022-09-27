from django.shortcuts import render, get_object_or_404, redirect

from webapp.models.category import Category


def category_edit_view(request, pk):
    if request.method == "GET":
        category = get_object_or_404(Category, pk=pk)
        return render(request, 'category_edit.html', context={'category': category})
    category_data = {
        'name': request.POST.get('text'),
        'description': request.POST.get('description')
    }
    print(category_data)
    category = get_object_or_404(Category, pk=pk)
    category.name = category_data['name']
    category.description = category_data['description']
    category.save()
    return redirect('category', pk=category.pk)
