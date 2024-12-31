from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username or Password')
            return redirect('/auth/login/')
        
        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, "Invalid Username or Password")
            return redirect('/auth/login/')
        
        login(request, user)
        return redirect('/home/')

    return render(request, 'login.html')

def register_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request, "Username already taken")
            return redirect('/auth/register/')
        
        user = User.objects.create_user(username=username)

        user.set_password(password)
        user.save()

        messages.info(request, f"Account: {username} created successfully")
        return redirect('/auth/register/')
    return render(request, 'register.html')
