from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth import authenticate, login

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid")

    return render(request,"login.html")

def reg(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        password1 = request.POST.get('password1', '')

        if not username or not first_name or not last_name or not email or not password or not password1:
            messages.error(request, "Please fill in all the required fields.")
            return render(request, "register.html", {'messages': messages.get_messages(request)})

        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists.")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already exists.")
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
                user.save()
                messages.success(request, "Registration successful. You can now log in.")
                return redirect('/authentication/login')
        else:
            messages.error(request, "Passwords do not match.")

    return render(request, "register.html", {'messages': messages.get_messages(request)})

def logout(request):
    auth.logout(request)
    return redirect('/')

