from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name='Название')

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, unique=True, verbose_name='Категории')
    price = models.PositiveIntegerField(default=0, verbose_name='Цена')
    year = models.PositiveSmallIntegerField(default=0)
    country = models.CharField(max_length=20, unique=True)
    city = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f'{self.city} - {self.year}'


class Comment(models.Model):
    user = models.CharField(max_length=20, null=True, blank=True)
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, unique=True)

    def __str__(self):
        return f'{self.product} - {self.text} - {self.user}'