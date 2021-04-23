from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'customer/index.html')

def loginpage(request):
    return render(request,'customer/index.html')

def user_login(request):
    if request.method == 'POST':
            mail = request.POST.get('email', '')
            user_password = request.POST.get('pass', '')
            user = authenticate(username=mail, password=user_password)
            if user is not None:
                login(request, user)
                return redirect('/shop')
            else:
                messages.warning(request, 'Invalid credentials')
                return redirect('/loginpage')

def user_signup(request):
    if request.method=='POST':
        mail = request.POST.get('email', '')
        userCheck = User.objects.filter(email=mail)
        if userCheck:
            messages.error(request, 'Email already exist')
            return redirect('/signuppage')
        fname = request.POST.get('first_name', '')
        lname=request.POST.get('last_name','')
        name=fname+' '+lname
        password = request.POST.get('password', '')
        contact=request.POST.get('phone')
        user_obj = User.objects.create_user(first_name=name, password=password,
                                                email=mail, username=mail)
        user_obj.save()
        userlog = authenticate(username=mail, password=password)

        login(request, userlog)
        return redirect('/')

def user_logout(request):
    logout(request)
    return redirect('/')