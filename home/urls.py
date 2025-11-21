from django.urls import path
from .views import *
from django.conf import settings
from home import views
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('',HomePage ),
    path('about/',AboutPage),
    path('Products/',ProductsPage),
    path('cart/',CartPage),

    path('login/', views.login_user, name='login'),
    path('signup/', views.signup_user, name='signup'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile_page, name='profile'),

]
