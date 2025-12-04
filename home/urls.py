from django.urls import path
from .views import *
from django.conf import settings
from home import views
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('home/',HomePage ),
    path('about/',AboutPage),
    path('Products/',ProductsPage),
    path('cart/',CartPage),
    # path('profile/',ProfilePage)
    path('profile/', views.profile_page, name="profile_page"),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    


]
