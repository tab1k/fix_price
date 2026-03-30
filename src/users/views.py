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
    return render(request, 'users/orders.html', {'user': request.user})


@login_required
def favorites(request):
    return render(request, 'users/favorites.html', {'user': request.user})


@login_required
def cart(request):
    return render(request, 'users/cart.html', {'user': request.user})
