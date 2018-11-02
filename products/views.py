import json
from django.shortcuts import render
import datetime

def product_list(request):
    context = {}


    with open('products/data/products.json', 'r') as file:
        context = json.load(file)


    return render(request, 'products/list.html', context)


def product_detail(request, idx):
    context = {}


    with open('products/data/products.json', 'r') as file:
        context = json.load(file)


    return render(
        request,
        'products/detail.html',
        {
            'object': context['products'][idx]
        } )