from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


def product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'product_detail.html', {'product': product})


def product_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        new_product = Product(name=name, description=description, price=price)
        new_product.save()
        return redirect('product_list')
    return render(request, 'product_create.html')


def product_update(request, product_id):
    product = Product.objects.get(pk=product_id)
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.description = request.POST.get('description')
        product.price = request.POST.get('price')
        product.save()
        return redirect('product_list')
    return render(request, 'product_update.html', {'product': product})


def product_delete(request, product_id):
    product = Product.objects.get(pk=product_id)
    product.delete()
    return redirect('product_list')
