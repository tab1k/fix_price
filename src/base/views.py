from django.shortcuts import render
from store.models import Category, Product
from django.views import View

# Create your views here.
class HomePageView(View):

    def get(self, request):
        categories = Category.objects.all()[:4]
        products = Product.objects.all()
        return render(request, 'base/index.html', {'categories': categories, 'products':products})

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
    return render(request, 'base/market.html')

def sale(request):
    return render(request, 'base/sale.html')

def help_page(request):
    return render(request, 'base/help.html')
