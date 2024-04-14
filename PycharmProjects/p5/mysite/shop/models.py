from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name='Названия')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    text = models.TextField(blank=True, null=True, verbose_name='Техт')
    price = models.PositiveSmallIntegerField(default=0, verbose_name='Цена')
    date = models.DateField(auto_now_add=False, verbose_name='Дата')
    image = models.ImageField(upload_to='img/', null=True, blank=True, verbose_name='Для фото')
    CHOICES_BOX = (
        ('Мужское', 'Мужское'),
        ('Женские', 'Женские'),
        ('Другое', 'Другое')
    )
    box = models.CharField(max_length=16, choices=CHOICES_BOX, default='Мужское', verbose_name='Выбрать')
    stock = models.IntegerField(default=2)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.CharField(max_length=16)
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} - {self.product}'

