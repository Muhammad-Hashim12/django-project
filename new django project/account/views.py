from django.shortcuts import render,redirect

from django.contrib.auth.models import User,auth

from django.contrib import messages

# Create your views here.

def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        user_name=request.POST['user_name']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request,'username already exist')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already exist')
                return redirect('register')
            elif not User.objects.filter(username=user_name,first_name=first_name,last_name=last_name,email=email,password=password1).exists():
                messages.info(request,'fill all the details')
                return redirect('register')
            else:    
                user= User.objects.create_user(first_name=first_name,last_name=last_name,username=user_name,email=email,password=password1)
                user.save();
                messages.success(request, "Profile details updated.")
                return redirect('login')
    else:
        return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user= auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'invalid username or password')
            return redirect('login')
    
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')