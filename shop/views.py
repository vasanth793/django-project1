from django.shortcuts import render, get_object_or_404, redirect
from .models import Product

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    images = product.images.all()  # product->ProductImage
    return render(request, "product_detail.html", {
        "product": product,
        "images": images
    })


# SIMPLE CART (session)
def add_to_cart(request, id):
    cart = request.session.get("cart", [])

    if id not in cart:
        cart.append(id)

    request.session["cart"] = cart

    return redirect("product_detail", id=id)
