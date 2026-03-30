from django.urls import path
from .views import *

app_name = 'store'

urlpatterns = [
    path('category/<slug:slug>/', CategoryDetailView.as_view(), name='category'),
    path('product/<slug:slug>/', ProductDetailView.as_view(), name='product'),
]
