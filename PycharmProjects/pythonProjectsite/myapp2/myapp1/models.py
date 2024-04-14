from django.db import models


class Marca(models.Model):
    name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.name


class Model(models.Model):
    name = models.CharField(max_length=16, unique=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} : {self.marca}'


class Car(models.Model):
    title = models.CharField(max_length=32)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    year = models.DateField()
    CHOICES_BOX = (
        ('Автомат', 'Автомат'),
        ('Механика', 'Механика'),
    )
    box = models.CharField(max_length=16, choices=CHOICES_BOX)

    def __str__(self):
        return self.title


class CarPhoto(models.Model):
    image = models.ImageField(upload_to='img', null=True, blank=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)


class Comment(models.Model):
    user = models.CharField(max_length=16)
    text = models.TextField()
    date = models.DateTimeField(auto_now=16)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} - {self.car}'