from django.urls import path

from .views import CustomLoginView, RegisterView, favorites, logout, orders, profile

app_name = 'users'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('orders/', orders, name='orders'),
    path('favorites/', favorites, name='favorites'),
]
