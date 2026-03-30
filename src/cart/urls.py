from django.urls import path

from .views import AddToCartView, CartListView, RemoveFromCartView

app_name = 'cart'

urlpatterns = [
    path('', CartListView.as_view(), name='cart_list'),
    path('add/<int:product_id>/', AddToCartView.as_view(), name='add_to_cart'),
    path('remove/<int:item_id>/', RemoveFromCartView.as_view(), name='remove_from_cart'),
]
