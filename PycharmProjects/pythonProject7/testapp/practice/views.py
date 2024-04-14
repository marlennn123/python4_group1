from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import ProductForm


def product_list(request):
    category = Category.objects.all()
    product = Product.objects.all()

    if request.method == 'GET':
        query = request.GET.get('q')
        category = request.GET.get('category')
        product = request.GET.get('product')

        if query:
            category = category.filter(title__icontains=query) | category.filter(description__icontains=query)

        if product:
            product = product.filter(marka__name=product)

    return render(request, 'product_list.html', {'product': product, 'category': category})


def product_detail(request, pk):
    product = Product.objects.filter(pk=pk)
    comment = Comment.objects.filter(pk=pk)
    photos = ProductPhoto.objects.all()
    return render(request, 'product_detail.html', {'products': product, 'comments': comment, 'photos': photos})


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')

    else:
        form = ProductForm()
    return render(request, 'product_create.html', {'form': form})


def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)

    return render(request, 'product_update.html', {'form': form})


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'PIST':
            product.delete()
            return redirect('product_list')
    return render(request, 'product_delete.html', {'product': product})

