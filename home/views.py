from django.shortcuts import render, redirect
from .models import Product
# Create your views here.


def homepage(request, *args, **kwargs):
    data = Product.objects.all()
    context = {
        "data": data,
    }
    return render(request, "home.html", context)


def add_product(request, *args, **kwargs):
    if request.method == "POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        reg = Product(
            name=name,
            price=price,
            description=description,
        )
        reg.save()
        return redirect('/')
    return render(request, "add.html", {})


def edit_product(request, product_id, *args, **kwargs):
    data = Product.objects.get(id=product_id)
    if request.method == "POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        data.name = name
        data.price = price
        data.description = description
        data.save()
        return redirect('/')
    context = {
        "data": data,
    }
    return render(request, "edit.html", context)


def delete_product(request, product_id, *args, **kwargs):
    data = Product.objects.get(id=product_id)
    data.delete()
    return redirect('/')
