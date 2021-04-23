from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index,name='home'),
    path('customer/',include('customer.urls')),
    path('restro/',include('restro.urls')),
    path('valet/',include('valet.urls')),
]
