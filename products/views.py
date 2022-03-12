from django.shortcuts import render
from .models import Product


def all_products(request):
    '''
    A view to show all products.
    Including sorting and searching queries.
    '''
    products = Product.objects.all()

    context = {
        'prodcuts': products,
    }

    return render(request, 'products/products.html', context)
