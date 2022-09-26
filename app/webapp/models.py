from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='Category', max_length=200, null=False, blank=False)
    description = models.TextField(verbose_name='Description', max_length=1000, null=True)
    created_at = models.DateField(verbose_name='Create date', auto_now_add=True)
    update_at = models.DateField(verbose_name='Update date', auto_now=True, null=True)


class Product(models.Model):
    name = models.CharField(verbose_name='Product', max_length=200, null=False, blank=False)
    description = models.TextField(verbose_name='Description', max_length=1000, null=True)
    category = models.ForeignKey(verbose_name='Category', to='webapp.Category', null=False, blank=False, related_name='product', on_delete=models.RESTRICT)
    created_at = models.DateTimeField(verbose_name='Create date', auto_now_add=True)
    price = models.DecimalField(verbose_name="Price", decimal_places=2, max_digits=10, null=False, blank=False)
    picture = models.CharField(verbose_name='Picture', max_length=1000, null=True, blank=False)
    update_at = models.DateField(verbose_name='Update date', auto_now=True, null=True)


class Meta:
    verbose_name = "Category"
    verbose_name_plural = "cCategories"
