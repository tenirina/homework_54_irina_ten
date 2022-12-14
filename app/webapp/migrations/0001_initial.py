# Generated by Django 4.1.1 on 2022-09-26 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Category')),
                ('description', models.TextField(max_length=1000, null=True, verbose_name='Description')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Create date')),
                ('update_at', models.DateField(auto_now=True, null=True, verbose_name='Update date')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Product')),
                ('description', models.TextField(max_length=1000, null=True, verbose_name='Description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Create date')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('picture', models.CharField(max_length=50, null=True, verbose_name='Picture')),
                ('update_at', models.DateField(auto_now=True, null=True, verbose_name='Update date')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='product', to='webapp.category', verbose_name='Category')),
            ],
        ),
    ]
