from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=16)
    year = models.DateField()
    price = models.PositiveIntegerField(default=0)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    deliver = (
        ('Доставка', 'Доставка'),
        ('Самовызов', 'Самовызов'),
    )
    box = models.CharField(max_length=16, choices=deliver)

    def __str__(self):
        return self.title


class ProductPhoto(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='img/', null=True, blank=True)

    def __str__(self):
        return f'{self.product}'


class Comment(models.Model):
    autor = models.CharField(max_length=16)
    text = models.TextField()
    date = models.DateTimeField(auto_now=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.autor} - {self.product}'


