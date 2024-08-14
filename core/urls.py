from django.urls import path
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .views import (
    remove_from_cart,
    reduce_quantity_item,
    add_to_cart,
    ProductView,
    HomeView,
    LoginView,
    OrderSummaryView,
    CheckoutView,
    PaymentView
)

# def LoginView(request):
#     return render(request, "login.html")

def logoutView(request):
    logout(request)
    return redirect("/")

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    # path('', HomeView.as_view(), name='login'),
    path('product/<pk>/', ProductView.as_view(), name='product'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('add-to-cart/<pk>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<pk>/', remove_from_cart, name='remove-from-cart'),
    path('reduce-quantity-item/<pk>/', reduce_quantity_item, name='reduce-quantity-item'),
    path('accounts/login/', LoginView.as_view(), name='login')
    
]


