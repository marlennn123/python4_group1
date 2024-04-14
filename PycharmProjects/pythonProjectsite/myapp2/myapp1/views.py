from django.shortcuts import render, redirect, get_object_or_404
from .models import Car, Comment, CarPhoto, Marca, Model
from .forms import CarForm


def car_list(request):
    markas = Marca.objects.all()
    models = Model.objects.all()
    cars = Car.objects.all()

    if request.method == 'GET':
        query = request.GET.get('q')
        marka = request.GET.get('marka')
        model = request.GET.get('model')
        price_from = request.GET.get('price_from')
        price_to = request.GET.get('price_to')

        if query:
            cars = cars.filter(title__icontains=query) | cars.filter(description__icontains=query)

        if marka:
            cars = cars.filter(marka__name=marka)

        if model:
            cars = cars.filter(model__name=model)

        if price_from:
            cars = cars.filter(price__gte=price_from)

        if price_to:
            cars = cars.filter(price__lte=price_to)

    return render(request, 'car_list.html', {'cars': cars, 'markas': markas, 'models': models})



def car_detail(request, pk):
    car = Car.objects.get(pk=pk)
    photos = CarPhoto.objects.filter(car=car)
    comments = Comment.objects.filter(car=car)
    return render(request, 'car_detail.html', {'car': car, 'photos': photos, 'comments': comments})


def car_create(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('car_list')

    else:
        form = CarForm()
    return render(request, 'car_create.html', {'form': form})


def car_update(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarForm(instance=car)
    return render(request, 'car_update.html', {'form': form})


def car_delete(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'PIST':
            car.delete()
            return redirect('car_list')
    return render(request, 'car_delete.html', {'car': car})
