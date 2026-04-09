from django.shortcuts import render
from store.models import Category, Product
from django.views import View


NEW_PRODUCTS_LIMIT = 8
FEATURED_PRODUCTS_LIMIT = 8

# Create your views here.
class HomePageView(View):

    def get(self, request):
        categories = Category.objects.all()[:6]
        new_products = Product.objects.filter(avaliable=True).order_by('-created_at')[:NEW_PRODUCTS_LIMIT]
        featured_products = Product.objects.filter(avaliable=True).order_by('-updated_at')[:FEATURED_PRODUCTS_LIMIT]

        context = {
            'categories': categories,
            'new_products': new_products,
            'featured_products': featured_products,
        }
        return render(request, 'base/index.html', context)

    def post(self, request):
        pass

"""
def get_base_page(request):
    categories = Category.objects.all()[:4]
    products = Product.objects.all()
    return render(request, 'base/index.html', {'categories': categories, 'products':products})
"""

def about_us(request):
    return render(request, 'base/about_us.html')

def market(request):
    categories = Category.objects.all()
    return render(request, 'base/market.html', {'categories': categories})

def sale(request):
    return render(request, 'base/sale.html')

def help_page(request):
    return render(request, 'base/help.html')
