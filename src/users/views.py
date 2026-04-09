from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import CreateView

from .forms import CustomUserCreationForm


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('base:home')

    def form_valid(self, form):
        response = super().form_valid(form)
        auth_login(self.request, self.object)
        return response


class CustomLoginView(LoginView):
    template_name = 'auth/login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('base:home')
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('base:home')

        return render(request, self.template_name, {
            'error': 'Неверный email или пароль',
        })


@require_POST
def logout(request):
    auth_logout(request)
    return redirect('base:home')


@login_required
def profile(request):
    return render(request, 'users/profile.html', {'user': request.user})


@login_required
def orders(request):
    demo_orders = [
        {
            'image': 'images/банан.png',
            'title': 'Бананы, 1кг.',
            'quantity': '20 шт.',
            'price': '500 ₸',
            'status': 'Доставляется',
            'status_icon': 'fa-refresh',
            'date': '29/05/2022',
            'address': 'Алматы, проспект Назарбаева, 58',
            'seller': 'ТехноGRAD',
        },
        {
            'image': 'images/банан.png',
            'title': 'Бананы, 1кг.',
            'quantity': '20 шт.',
            'price': '500 ₸',
            'status': 'Доставлено',
            'status_icon': 'fa-check',
            'date': '29/05/2022',
            'address': 'Алматы, проспект Назарбаева, 58',
            'seller': 'ТехноGRAD',
        },
        {
            'image': 'images/банан.png',
            'title': 'Бананы, 1кг.',
            'quantity': '20 шт.',
            'price': '500 ₸',
            'status': 'Доставляется',
            'status_icon': 'fa-check',
            'date': '29/05/2022',
            'address': 'Алматы, проспект Назарбаева, 58',
            'seller': 'ТехноGRAD',
        },
    ]
    return render(request, 'users/orders.html', {'user': request.user, 'orders': demo_orders})


@login_required
def favorites(request):
    demo_favorites = [
        {
            'image': 'images/rafaello.png',
            'name': 'Rafaello',
            'desc': 'lorem ipsum lorem ipsum lorem ipsum lorem ipsum',
            'volume': '300 ml',
            'price': '700 ₸',
        },
        {
            'image': 'images/rafaello.png',
            'name': 'Rafaello',
            'desc': 'lorem ipsum lorem ipsum lorem ipsum lorem ipsum',
            'volume': '300 ml',
            'price': '700 ₸',
        },
        {
            'image': 'images/rafaello.png',
            'name': 'Rafaello',
            'desc': 'lorem ipsum lorem ipsum lorem ipsum lorem ipsum',
            'volume': '300 ml',
            'price': '700 ₸',
        },
        {
            'image': 'images/rafaello.png',
            'name': 'Rafaello',
            'desc': 'lorem ipsum lorem ipsum lorem ipsum lorem ipsum',
            'volume': '300 ml',
            'price': '700 ₸',
        },
    ]
    return render(request, 'users/favorites.html', {'user': request.user, 'favorites': demo_favorites})


@login_required
def cart(request):
    return render(request, 'users/cart.html', {'user': request.user})
