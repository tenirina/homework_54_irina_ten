# Generated by Django 4.1.1 on 2022-09-27 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(choices=[], on_delete=django.db.models.deletion.RESTRICT, related_name='product', to='webapp.category', verbose_name='Category'),
        ),
    ]
