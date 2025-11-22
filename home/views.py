from django.shortcuts import render, redirect,get_object_or_404
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

def ProfilePage(request):

    return render(request,'profile.html')



def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)

    # Load session list
    viewed = request.session.get("recently_viewed", [])

    # If product already exists, remove it
    if product_id in viewed:
        viewed.remove(product_id)

    # Add product at front (latest first)
    viewed.insert(0, product_id)

    # Keep only last 10 items
    viewed = viewed[:10]

    # Save back to session
    request.session["recently_viewed"] = viewed

    return render(request, "home/product_detail.html", {
        "product": product
    })

from home.models import Product

def profile_page(request):
    # Get viewed IDs
    viewed_ids = request.session.get("recently_viewed", [])

    recent_products = Product.objects.filter(id__in=viewed_ids)

    return render(request, "profile.html", {
        "recent_products": recent_products,
    })
