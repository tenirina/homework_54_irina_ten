# Generated by Django 4.1.1 on 2022-09-26 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.CharField(max_length=1000, null=True, verbose_name='Picture'),
        ),
    ]
