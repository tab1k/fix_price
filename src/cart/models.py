from django.db import models
from users.models import CustomUser
from store.models import Product


class Cart(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Корзина пользователя {self.user.email}'

    def get_total_price(self):
        return sum(item.get_total_price() for item in self.items.all())

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} x {self.product.name} в корзине {self.cart.user.email}'

    def get_total_price(self):
        return self.quantity * self.product.price

    class Meta:
        verbose_name = 'Товар корзины'
        verbose_name_plural = 'Товары корзины'
