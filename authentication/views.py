
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from authentication.models import User        # ✔ CORRECT
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def LoginPage(request):

    context = {
        "error" : ""
    }

    if request.method == "POST":

        print(request.POST)

        user = authenticate (username= request.POST["username"] , password= request.POST['password'])

        print(user)

        if user is not None :

            login(request,user)

            return redirect('/login/login/')
        
        else:

            context ={
                "error" : "invalid Username or Password"
            }
            return render(request,'login.html',context)


    return render(request, 'login.html',context)

def LogoutPage(request):

    logout(request)

    return redirect('/login/login/')


def SignupPage(request):

    if request.method == "POST":

        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email_address']
        password = request.POST['password']

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )

        user.first_name = first_name
        user.last_name = last_name
        user.save()

        return redirect('/login/login/')

    return render(request, 'signup.html')
