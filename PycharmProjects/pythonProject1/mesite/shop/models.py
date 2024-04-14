from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    created_date = models.DateField()
    active = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.price


class Comment(models.Model):
    author = models.CharField(max_length=16)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author} - {self.product}'