from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login

# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        confirmpassword = request.POST.get('password2')

        if password != confirmpassword:
            messages.error(request,"password did not match")
            return redirect('register')

        if User.objects.filter(username=username):
            messages.error(request,"username already exists")
            return redirect('register')

        if User.objects.filter(email=email):
            messages.error(request,"email has already been used for an existing account")
            return redirect('register')
        
        if len(username)>15:
            messages.error(request,"the username is too long")
            return redirect('register')


        user = User.objects.create_user(username,email,password)
        user.first_name = firstname
        user.last_name = lastname
        user.save()
        messages.success(request, "you have registered successfully ")
        return redirect('/login')
    return render(request,'users/registration.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, "you have successfully logged in")
            # context = {
            #     'user':user
            # }
            return redirect("myapp:home")
        else:
            messages.error(request, "incorrect password or username")
            return redirect('/login')    
    return render(request,'users/login.html')

def leave(request):
    logout(request)
    return redirect('/login')
