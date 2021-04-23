
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from customer.models import Order
from .models import Valet
# Create your views here.

# =================================================================================================================
def log_page(request):
    return render(request, 'valet/login.html')


def restro_login(request):
    if request.method == 'POST':
        mail = request.POST.get('email', '')
        user_password = request.POST.get('pass', '')
        user = authenticate(username=mail, password=user_password)
        valet=Valet.objects.filter(user=user)
        if valet:
            if user is not None:
                login(request, user)
                return redirect('/valet')
            else:
                messages.warning(request, 'Invalid credentials')
                return redirect('/valet/login')
        else:
            messages.warning(request, 'Invalid credentials')
            return redirect('/valet/login')


def user_logout(request):
    logout(request)
    return redirect('/valet/login')


# =================================================================================================================
def reg_page(request):
    return render(request, 'valet/signup.html')


def register(request):
    if request.method == 'POST':
        password = request.POST.get('pass', '')
        re_password = request.POST.get('re_pass', '')
        if password == re_password:
            mail = request.POST.get('email', '')
            userCheck = User.objects.filter(email=mail)
            if userCheck:
                messages.warning(request, 'Email already exist')
                return redirect('/valet/register')

            name = request.POST.get('name', '')

            contact = request.POST.get('phone', '')

            city = request.POST.get('city', '')
            state = request.POST.get('stt', '')
            zipcode = request.POST.get('zip', '')

            id_proof=request.POST.get('url1')
            dp=request.POST.get('url')
            user_obj = User.objects.create_user(first_name=name, password=password, email=mail, username=mail)
            user_obj.save()
            userlog = authenticate(username=mail, password=password)
            valet=Valet(user=user_obj, city=city, state=state, zipcode=zipcode, phone=contact, dp=dp,id_proof=id_proof)
            valet.save()
            login(request, userlog)
            return redirect('/valet')
        else:
            messages.warning(request, 'Email already exist')
            return redirect('/valet/register')

#========================================================================================================================

def order(request):
    if request.user.is_authenticated:
        valet=Valet.objects.get(user=request.user)
        if valet.free:
            orders=Order.objects.filter(recv_by_customer=False, accept_by_valet=False)
            art=[]
            for i in orders:
                if i.customer.city==valet.city:
                    art.append(i)

            return render(request,'valet/orders.html',{'orders':art})
        else:
            messages.warning(request, 'Already on a Delivery! Complete it')
            return redirect('/valet/my')
    else:
        return redirect('/valet/login')

def complete(request,order_id):
    if request.user.is_authenticated:
        if request.method=="POST":
            order=Order.objects.get(id=order_id)
            otp=int(request.POST.get('otp'))
            if otp==order.otp_customer:
                order.recv_by_customer=True
                order.save()
                valet=Valet.objects.get(user=request.user)
                valet.free=True
                valet.save()
                return redirect('/valet/')
            else:
                messages.warning(request, 'Incorrect OTP!')
                return redirect('/valet/my')
    else:
        return redirect('/valet/login')

def accept(request,order_id):
    if request.user.is_authenticated:
        valet=Valet.objects.get(user=request.user)
        order = Order.objects.get(id=order_id)
        order.valet=valet
        order.accept_by_valet=True
        order.save()
        valet.free=False
        valet.save()
        return redirect('/valet/my')
    else:
        return redirect('/valet/login')


def my_orders(request):
    if request.user.is_authenticated:
        valet = Valet.objects.get(user=request.user)
        order = Order.objects.get(valet=valet, recv_by_customer=False)
        return render(request, 'valet/my_order.html',{'i':order})
    else:
        return redirect('/valet/login')
