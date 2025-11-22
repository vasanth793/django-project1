
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from .models import User

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

            return redirect('/profile/')
        
        else:

            context ={
                "error" : "invalid Username or Password"
            }
            return render(request,'login.html',context)


    return render(request, 'login.html',context)

def LogoutPage(request):

    logout(request)

    return redirect('/login/login/')

