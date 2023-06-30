from django.shortcuts import get_object_or_404, render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Sales
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

#Create your views here.


def HomePage(request):
    sales = Sales.objects.all()
    if request.method == 'GET':
        brand = request.GET.get('brand')
        if brand:
            products = Sales.objects.all().filter(brand__icontains = brand)

            return render(request, 'search.html', {"products": products})
        else:
            return render(request, 'home.html', {"home": sales})
    


def ProfilePage(request, count=5):
    # viewed_sales = request.session.get('viewed_sales', []) 
    # search = request.session.get('search_history', []) 
    # last_viewed_sales = [] 
    # for sales_id in viewed_sales[:count]: 
    #     sales = get_object_or_404(sales, pk=sales_id) 
    #     last_viewed_sales.append(sales) 
    # return render(request, 'profile.html', {'last_viewed_sales': last_viewed_sales, 'search_history': search})
    return render(request, 'profile.html')


def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        
        user = User.objects.filter(username=uname)
        if pass1 != pass2:
            return HttpResponse("Your password and comform password are not same!")
        elif user.exists():
            return HttpResponse("Username already taken. Please enter a new one.")
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')
        
    return render(request, 'signup.html')

def LoginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')

        user = authenticate(request, username = username, password = pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or password is incorrect!")
            

    return render(request, 'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def AdminnPage(request):
    sales = Sales.objects.all()
    return render(request, 'adminn.html', {"home": sales})

def ApprovePage(request):
    return render(request, 'approve.html')

def CreateProductPage(request):
    # sales = get_object_or_404(sales, pk=id) 
    # viewed_sales = request.session.get('viewed_sales', []) 
    # if id not in viewed_sales: 
    #     viewed_sales.insert(0, id) 
    # request.session['viewed_sales'] = viewed_sales 
    # return render(request, 'create_product.html', {'sales': sales})
    return render(request, 'create_product.html')

def UsersPage(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {"users": users})

def EditProfilePage(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        return render(request, 'edit_profile.html')

def SearchPage(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            products = Sales.objects.all().filter(brand__icontains = query)

            return render(request, 'search.html', {"products": products})
        else:
            return render(request, 'search.html', {})