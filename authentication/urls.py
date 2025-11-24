from django.urls import path
from .views import *

urlpatterns = [

    path('login/', LoginPage),
    path('logout/', LogoutPage),
    path('signup/', SignupPage),
]