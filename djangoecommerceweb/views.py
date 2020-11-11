from django.shortcuts import render
from djangoecommerceweb.models import Product

def ecommerce_index(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'ecommerce_index.html', context)

def ecommerce_detail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product': product
    }
    return render(request, 'ecommerce_detail.html', context)

