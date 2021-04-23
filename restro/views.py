from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Restro, Menu, Tiffin_Menu
from customer.models import Order, Reservation

# Create your views here.

# =================================================================================================================
def log_page(request):
    return render(request, 'restro/login.html')


def restro_login(request):
    if request.method == 'POST':
        mail = request.POST.get('email', '')
        user_password = request.POST.get('pass', '')
        user = authenticate(username=mail, password=user_password)
        restro=Restro.objects.filter(user=user)
        if restro:
            if user is not None:
                login(request, user)
                return redirect('/restro')
            else:
                messages.warning(request, 'Invalid credentials')
                return redirect('/restro/login')
        else:
            messages.warning(request, 'Invalid credentials')
            return redirect('/restro/login')


def user_logout(request):
    logout(request)
    return redirect('/restro/login')


# =================================================================================================================
def reg_page(request):
    return render(request, 'restro/signup.html')


def register(request):
    if request.method == 'POST':
        password = request.POST.get('pass', '')
        re_password = request.POST.get('re_pass', '')
        if password == re_password:
            mail = request.POST.get('email', '')
            userCheck = User.objects.filter(email=mail)
            if userCheck:
                messages.warning(request, 'Email already exist')
                return redirect('/restro/register')

            name = request.POST.get('restro_name', '')

            owner_name = request.POST.get('owner_name', '')
            owner_phone = request.POST.get('owner_phone', '')
            contact = request.POST.get('phone', '')

            city = request.POST.get('city', '')
            state = request.POST.get('stt', '')
            zipcode = request.POST.get('zip', '')
            address = request.POST.get('address', '')

            user_obj = User.objects.create_user(first_name=name, password=password,
                                                email=mail, username=mail)
            user_obj.save()
            userlog = authenticate(username=mail, password=password)
            restro = Restro(user=user_obj,name=name, owner=owner_name, city=city, state=state, address=address, zipcode=zipcode,
                            phone=contact, owner_phone=owner_phone)
            restro.save()
            login(request, userlog)
            return redirect('/restro')
        else:
            messages.warning(request, 'Email already exist')
            return redirect('/restro/register')


# ===============================================================================================================================
def menu(request):
    # =============render dish page=======
    return render(request, 'restro/create_menu.html')

def menu_create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            dish_name = request.POST.get('dish', '')
            price = request.POST.get('price', '')
            desc = request.POST.get('desc', '')
            photo = request.POST.get('url', '')
            #restro = Restro.objects.get(user=request.user)
            menu = Menu(restro=request.user, dish=dish_name, price=price, desc=desc, photo=photo)
            menu.save()
            return redirect('/restro/menu')
    else:
        return redirect('/restro/login')

def view_menu(request):
    if request.user.is_authenticated:

        menu = Menu.objects.filter(restro=request.user)
        return render(request, 'restro/menu_view.html', {'menu': menu})
    else:
        return redirect('/restro/login')
# ========================================================================================================================

def orders(request):
    if request.user.is_authenticated:
        rest=Restro.objects.get(user=request.user)
        order=Order.objects.filter(restro=rest, recv_by_valet=False)
        return render(request,'restro/orders.html',{'orders':order})
    else:
        return redirect('/restro/login')


def complete(request, order_id):
    if request.user.is_authenticated:
        if request.method=='POST':
            order=Order.objects.get(id=order_id)
            otp1=int(request.POST.get('otp'))

            if otp1 == order.otp_restro:
                order.recv_by_valet=True
                order.save()
            else:
                messages.warning(request, 'Incorrect OTP')
            return redirect('/restro/orders')
    else:
        return redirect('/restro/login')

def prepared(request,order_id):
    if request.user.is_authenticated:
        order=Order.objects.get(id=order_id)
        order.prepared=True
        order.save()
        return redirect('/restro/orders')
    else:
        return redirect('/restro/login')


def reserve(request):
    if request.user.is_authenticated:
        rest=Restro.objects.get(user=request.user)
        res=Reservation.objects.filter(restro=rest, complete=False).order_by('date','time')
        return render(request,'restro/reserve.html',{'reserve':res})
    else:
        return redirect('/restro/login')

def book(request,res_id):
    if request.user.is_authenticated:
        if request.method=='POST':
            otp=int(request.POST.get('otp'))
            reservation=Reservation.objects.get(id=res_id)
            if otp==reservation.otp:
                reservation.complete=True
                reservation.save()
                return redirect('/restro/reserve')
            else:
                messages.warning(request,'Incorrect OTP!')
                return redirect('/restro/reserve')
    else:
        return redirect('/restro/login')

#======================================================================================================================================

def tiffin_menu(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            m_bf = request.POST.get('m_bf')
            m_lun = request.POST.get('m_lun')
            m_din = request.POST.get('m_din')

            tu_bf = request.POST.get('tu_bf')
            tu_lun = request.POST.get('tu_lun')
            tu_din = request.POST.get('tu_din')

            w_bf = request.POST.get('w_bf')
            w_lun = request.POST.get('w_lun')
            w_din = request.POST.get('w_din')

            th_bf = request.POST.get('th_bf')
            th_lun = request.POST.get('th_lun')
            th_din = request.POST.get('th_din')

            f_bf = request.POST.get('f_bf')
            f_lun = request.POST.get('f_lun')
            f_din = request.POST.get('f_din')

            sa_bf = request.POST.get('sa_bf')
            sa_lun = request.POST.get('sa_lun')
            sa_din = request.POST.get('sa_din')

            s_bf = request.POST.get('s_bf')
            s_lun = request.POST.get('s_lun')
            s_din = request.POST.get('s_din')