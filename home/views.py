from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Product



# Create your views here.

def HomePage(request):

    context = {
        'name' : 'vasanth'
    }


    return render(request,'index.html', context)

def AboutPage(request):

    context = {
        'name' : 'vasanth'
    }


    return render(request,'about.html', context)

def ProductsPage(request):

    context = {
        'name' : 'vasanth'
    }


    return render(request,'products.html', context)

def CartPage(request):

    return render(request,'cart.html')


# Signup / Register
def signup_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')

        if password != confirm:
            messages.error(request, "Passwords do not match")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('signup')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Account created successfully. Login now!")
        return redirect('login')

    return render(request, 'signup.html')


# Login
def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully")
            return redirect('profile')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')

    return render(request, 'login.html')


# Logout
def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('login')


# Profile (Protected)
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def profile_page(request):
    return render(request, 'profile.html')


# # Show all products
# def home_page(request):
#     products = Product.objects.all()
#     return render(request, "home/home.html", {"products": products})

# # Add to cart
# def add_to_cart_view(request, product_id):
#     add_to_cart(request, product_id)
#     return redirect("cart_page")

# # Show cart items
# def cart_page(request):
#     items, total = cart_items(request)
#     return render(request, "home/cart.html", {"items": items, "total": total})

# # Remove specific item
# def remove_cart_view(request, product_id):
#     remove_item(request, product_id)
#     return redirect("cart_page")
