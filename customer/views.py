from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Customer, Order, Reservation
from restro.models import Menu,Restro
from valet.models import Valet
import random
# Create your views here.
def signup(request):
    return render(request,'customer/signup.html')

def loginpage(request):
    return render(request,'customer/login.html')

def user_login(request):
    if request.method == 'POST':
            mail = request.POST.get('email', '')
            user_password = request.POST.get('pass', '')
            user = authenticate(username=mail, password=user_password)
            customer=Customer.objects.filter(user=user)
            if user is not None:
                if customer:
                    login(request, user)
                    return redirect('/customer/home')

            messages.warning(request, 'Invalid credentials')
            return redirect('/customer/login')

def user_signup(request):
    if request.method=='POST':
        password = request.POST.get('password', '')
        cnf_password = request.POST.get('confirm_password', '')
        if password==cnf_password:
            mail = request.POST.get('email', '')
            userCheck = User.objects.filter(email=mail)
            if userCheck:
                messages.warning(request, 'Email already exist')
                return redirect('/customer')
            fname = request.POST.get('first_name', '')
            lname=request.POST.get('last_name','')

            city = request.POST.get('city', '')
            city.replace(" ","")
            state = request.POST.get('stt', '')
            zipcode = request.POST.get('zip', '')
            address = request.POST.get('address', '')

            contact=request.POST.get('phone')
            user_obj = User.objects.create_user(first_name=fname,last_name=lname , password=password,
                                                    email=mail, username=mail)
            user_obj.save()
            custom=Customer(user=user_obj, phone=contact,city=city,zipcode=zipcode,address=address,state=state)
            custom.save()
            userlog = authenticate(username=mail, password=password)

            login(request, userlog)
            return redirect('/customer/home')

def user_logout(request):
    logout(request)
    return redirect('/customer')
#=========================================================================================================================
def searching(request):
    if request.user.is_authenticated:
        search=request.POST.get('search')
        cust=Customer.objects.get(user=request.user)
        restro=Restro.objects.filter(name=search, zipcode=cust.zipcode)

        return render(request,'customer/searching.html',{'restro':restro})
    else:
        return redirect('/customer/login')

def view_menu(request,rest):
    if request.user.is_authenticated:
        restro=Restro.objects.filter(user=rest)
        menu=Menu.objects.filter(restro=rest)
        return render(request,'customer/menu.html',{'menu':menu,'restro':restro[0],'user_log':rest})
    else:
        return redirect('/customer/login')

def checkout(request,custom):
    if request.user.is_authenticated:
        customer=Customer.objects.get(user=request.user)
        return render(request,'customer/checkout.html',{'user_log':custom,'customer':customer})
    else:
        return redirect('/customer/login')


def order(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            item=request.POST.get('itemsJson')
            amt=request.POST.get('amount')
            restro=request.POST.get('restro_name')
            rest=Restro.objects.get(user=restro)
            customer=Customer.objects.get(user=request.user)
            otp_valet=random.randint(100000,999999)
            otp_customer=random.randint(100000,999999)

            ord=Order(item=item,amt=amt,restro=rest,customer=customer,otp_restro=otp_valet,otp_customer=otp_customer)
            ord.save()


            return redirect('/customer/my_orders')
    else:
        return redirect('/customer/login')

def my_orders(request):
    if request.user.is_authenticated:
        user=request.user
        cust=Customer.objects.get(user=user)
        ord=Order.objects.filter(customer=cust).order_by('-date')
        return render(request,'customer/my_orders.html',{'orders':ord})
    else:
        return redirect('/customer/login')

def track_order(request):
    if request.user.is_authenticated:
        cust=Customer.objects.get(user=request.user)
        orders=Order.objects.filter(customer=cust,recv_by_customer=False).order_by('-date')
        if orders:
            return render(request,'customer/track.html',{'order':orders})
        else:
            messages.warning(request, 'No ongoing order')
            return redirect('/customer/my_orders')
    else:
        return redirect('/customer/login')

def index(request):
    custom=Customer.objects.get(user=request.user)
    rest = Restro.objects.filter(zipcode=custom.zipcode)
    params={'restro':rest}
    return render(request,'customer/index.html',params)

def book(request,restro_id):
    if request.user.is_authenticated:
        rest=Restro.objects.filter(id=restro_id)
        print(rest)
        if rest:
            rest=rest[0]
            customer = Customer.objects.get(user=request.user)
            reserve = Reservation.objects.filter(customer=customer).order_by('-date','-time')
            return render(request, 'customer/booking.html', {'reserve': reserve, 'rest': rest})
        else:
            return redirect('/customer/my_book')
    else:
        return redirect('/customer/login')

def booking(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            rest_id=request.POST.get('rest')
            restro=Restro.objects.get(id=rest_id)

            date=request.POST.get('date')
            time=request.POST.get('time')
            otp=random.randint(100000,999999)
            customer=Customer.objects.get(user=request.user)
            res=Reservation(customer= customer, restro=restro, date=date, time=time, otp=otp)
            res.save()
            return redirect('/customer/my_book')
    else:
        return redirect('/customer/login')

def my_book(request):
    if request.user.is_authenticated:
        customer = Customer.objects.get(user=request.user)
        reserve = Reservation.objects.filter(customer=customer).order_by('-date','-time')
        return render(request, 'customer/booking.html', {'reserve': reserve})
    else:
        return redirect('/customer/login')