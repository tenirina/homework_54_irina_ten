from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='Category', max_length=200, null=True, blank=False)
    description = models.TextField(verbose_name='Description', max_length=1000, null=True)
    created_at = models.DateTimeField(verbose_name='Create date', auto_now_add=True)
    update_at = models.DateTimeField(verbose_name='Update date', auto_now=True, null=True)
