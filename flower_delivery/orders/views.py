from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from .models import Product
import json

def product_list(request):
    products = Product.objects.all()
    return render(request, 'orders/product_list.html', {'products': products})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('product_list')
    else:
        form = SignUpForm()
    return render(request, 'orders/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('product_list')
    else:
        form = AuthenticationForm()
    return render(request, 'orders/login.html', {'form': form})

def checkout(request):
    if request.method == 'POST':
        cart_data = json.loads(request.POST['cart_data'])
        total_price = sum(int(item['price']) * item['quantity'] for item in cart_data.values())
        return render(request, 'checkout.html', {'cart_data': cart_data, 'total_price': total_price})
    return redirect('catalog')