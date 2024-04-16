from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name='Название')


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, unique=True, verbose_name='Категории')
    price = models.PositiveIntegerField(default=0, verbose_name='Цена')
    year = models.PositiveSmallIntegerField(default=0)
    country = models.CharField(max_length=20, unique=True)
    city = models.CharField(max_length=20, unique=True)


