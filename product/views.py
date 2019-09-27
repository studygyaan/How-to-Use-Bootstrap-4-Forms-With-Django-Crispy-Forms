from django.shortcuts import render

from django.views.generic import CreateView, UpdateView
from .models import Product
from .forms import ProductForm

class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'price')
    template_name = 'product.html'
    success_url = '/product-add/'

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product-update.html'