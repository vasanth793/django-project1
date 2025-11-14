from django.shortcuts import render

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