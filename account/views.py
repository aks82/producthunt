from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['Username'])
                return render(request,'signup.html',{'error':'Username already taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['Username'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request, 'signup.html', {'error': 'Passwords must match'})
    else:
        return render(request,'signup.html')

def login(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(username=request.POST['Username'])
            user = auth.authenticate(username=request.POST['Username'],password=request.POST['password'])
            if user is not None:
                auth.login(request, user)
                return redirect('home')
            else:
                return render(request,'login.html',{'error':'Authentication failed'})
        except User.DoesNotExist:
            return render(request, 'login.html', {'error': 'Username not found'})
    else:
        return render(request,'login.html')

def signout(request):
    if request.method == 'POST':
        auth.logout(request)
        return render(request, 'home.html')