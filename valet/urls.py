from django.urls import path,include
from . import views

urlpatterns = [
    #======================register=====================
    path('register', views.reg_page,name='reg_page'),
    path('registration', views.register,name='home'),
 #===========================login/logout=====================
    path('logging', views.restro_login,name='login'),
    path('login', views.log_page,name='log_page'),
    path('logout', views.user_logout,name='logout'),
    #==============================================================
    path('',views.order, name='orders'),
    path('my',views.my_orders, name='my  currnt orders'),
    path('complete/<str:order_id>',views.complete, name='orders cmplete'),
    path('accept/<str:order_id>',views.accept, name='orders accept'),
    ]