from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.views.generic import DetailView

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'store/category.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = self.object.products.filter(avaliable=True)
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/product.html'
    context_object_name = 'product'


"""

def get_category_page(request, slug=None):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.filter(avaliable=True)
    return render(
        request,
        'store/category.html',
        {'category': category, 'products': products},
    )

def get_product_page(request, slug=None):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/product.html', {'product': product})

"""
