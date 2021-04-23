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
 #=========================menu create=================
    path('create_menu', views.menu_create,name='create_menu'),
    path('menu', views.menu,name='menu'),
    path('', views.view_menu,name='view menu'),
    #=======================order view==================
    path('orders',views.orders,name='orders'),
    path('complete/<str:order_id>',views.complete,name='order completed'),
    path('prepared/<str:order_id>',views.prepared,name='order prepared'),
    #========================================================
    path('reserve',views.reserve,name='reserve'),
    path('book/<str:res_id>',views.book,name='book'),
]