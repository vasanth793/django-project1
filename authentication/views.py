
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from .models import User


def LoginPage(reqest):

    context = {
        "error":" "
    }

    if reqest.method == 'POST':

        print(reqest.POST)

        user = authenticate(
            
            username=reqest.POST['username'],
            password=reqest.POST['password']
        )
        print(user)

        if user is not None:

            login(reqest, user)

            return redirect('/orders/all/customers/')
        
        else:

            context ={
                "error":"username or password is incorrect"
            }

            return render(reqest, 'login.html',context)




    return render(reqest, 'login.html', context)

def LogoutUser(request):

    logout(request)

    return redirect('/')

def SignupPage(request):

    context ={
        "error":""

    }


    if request.method == "POST":
        user_check = User.objects.filter(username = request.POST['username'])

        if len(user_check) > 0:
            context = {
                "error": "*Username already exists*"
            }

            return render(request, 'signup.html',context)

   

        new_user = User(username = request.POST['username'],first_name = request.POST
        ['first_name'], last_name = request.POST['last_name'], email = request.POST['email_address'],
        age = request.POST['age'], )


        new_user.set_password(request.POST['password'])

        new_user.save()

        return redirect('/')




    return render (request, 'signup.html',context)