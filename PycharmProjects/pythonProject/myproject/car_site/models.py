from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.name


class Store(models.Model):
    title = models.CharField(max_length=32, verbose_name='Название')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    text = models.TextField()
    price = models.PositiveSmallIntegerField(default=0)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=16, verbose_name='Автор')
    text = models.TextField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='comment')
    parent_review = models.ForeignKey('self', related_name='replies', null=True, blank=True, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} - {self.store}'