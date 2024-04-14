from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.name


class Car(models.Model):
    title = models.CharField(max_length=32, verbose_name='Название')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    text = models.TextField()
    price = models.PositiveIntegerField(default=0)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=16, verbose_name='Автор')
    text = models.TextField()
    parent_review = models.ForeignKey('self', related_name='replies', null=True, blank=True, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} - {self.car}'
