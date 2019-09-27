from django.shortcuts import render

from django.views.generic import CreateView
from .models import Product

class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'price')
    template_name = 'product.html'