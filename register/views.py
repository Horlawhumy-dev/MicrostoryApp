from django.shortcuts import render, redirect
from .models import UserAccount
from django.contrib.auth import login, authenticate, logout
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User



# Create your views here.


def base_view(request):
    return render(request, 'register/base.html', {})


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home_app:index')
    else:
        if request.method == "POST":
            firstname = request.POST.get('first_name')
            lastname =  request.POST.get('last_name')
            username =  request.POST.get('username')
            email = request.POST.get('email')
            pass1 = request.POST.get('password1')
            pass2 = request.POST.get('password2')
            
            if pass1 == pass2:
                if User.objects.filter(username=username, email=email).exists():
                    messages.error(request, 'Username or Email already exist')
                    print("username or email already exist")
                    return redirect('register:signup')
                else:
                    user = User.objects.create_user(first_name = firstname, last_name=lastname, username=username, email=email, password=pass1)
                    user.save()
                    messages.success(request, 'Account was created successfully for ' + username)
                    return redirect('register:signin')
            else:
                messages.error(request, 'Passwords do not match')
                print("unmatched passwords")
                return redirect('register:signup')
        else:
            return render(request, 'register/account.html')
       
def signin_view(request):
    if request.user.is_authenticated:
            return redirect('home_app:index')
    else:
        if request.method == "POST":
            username =  request.POST.get('username')
            password =   request.POST.get('password1')
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'You are now logged in')
                return redirect('home_app:index')
            else:
                messages.error(request, 'Invalid credentials supplied')
                return redirect('register:signin')
        else:
            return render(request, 'register/signin.html')

def signout_view(request):
    logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('home_app:index')
