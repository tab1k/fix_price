from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView

from store.models import Product

from .models import Cart, CartItem
from datetime import datetime

def get_or_create_cart_for_user(user):
    cart, created = Cart.objects.get_or_create(user=user)
    return cart



class CartListView(LoginRequiredMixin, ListView):
    model = CartItem
    template_name = 'cart/cart_list.html'
    context_object_name = 'cart_items'

    def get_queryset(self):
        return CartItem.objects.filter(cart__user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = Cart.objects.filter(user=self.request.user).first()
        context['datetime'] = datetime.now()
        return context


class AddToCartView(LoginRequiredMixin, View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

        if not created:
            cart_item.quantity += 1
            cart_item.save()
            messages.success(request, f'Количество товара "{product.name}" в корзине увеличено.')
        else:
            messages.success(request, f'Товар "{product.name}" добавлен в корзину.')

        return redirect('cart:cart_list')


class RemoveFromCartView(LoginRequiredMixin, View):
    def post(self, request, item_id):
        cart_item = get_object_or_404(
            CartItem,
            id=item_id,
            cart__user=request.user,
        )
        product_name = cart_item.product.name
        cart_item.delete()

        messages.success(request, f'Товар "{product_name}" удален из корзины.')
        return redirect('cart:cart_list')
