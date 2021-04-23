from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.signup,name='home'),
    path('register', views.user_signup,name='registered'),
    path('login', views.loginpage,name='login page'),
    path('logging', views.user_login,name='login'),
    path('logout', views.user_logout,name='logout'),

    path('menu/<str:rest>',views.view_menu,name='view menu'),

    path('home', views.index, name='search page'),
    path('searching', views.searching, name='searching'),
    path('checkout/<str:custom>', views.checkout, name='checkout'),

    path('order',views.order,name='order'),
    path('my_orders',views.my_orders,name='my_order'),
    path('track',views.track_order,name='track'),


    path('book/<str:restro_id>',views.book,name='book'),
    path('booking',views.booking,name='booking'),
    path('my_book',views.my_book,name='my booking'),

]