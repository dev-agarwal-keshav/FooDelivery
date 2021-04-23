from django.db import models
from django.contrib.auth.models import User
from restro.models import Restro
from valet.models import Valet
# Create your models here.

DEFAULT_VALET_ID=1
class Customer(models.Model):
    user=models.ForeignKey(User, related_name='customer', on_delete=models.CASCADE)

    phone=models.IntegerField()
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    address=models.TextField(default='')
    zipcode=models.IntegerField()


class Order(models.Model):
    item=models.TextField()
    amt=models.IntegerField()

    restro=models.ForeignKey(Restro,related_name='restro',on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,related_name='customer_ordered',on_delete=models.CASCADE)
    valet=models.ForeignKey(Valet,related_name='valet',on_delete=models.CASCADE, default=DEFAULT_VALET_ID)

    recv_by_valet=models.BooleanField(default=False)
    recv_by_customer=models.BooleanField(default=False)

    date=models.DateTimeField(auto_now_add=True)

    accept_by_valet=models.BooleanField(default=False)
    prepared=models.BooleanField(default=False)

    otp_restro=models.IntegerField(default=0)
    otp_customer=models.IntegerField(default=0)


class Reservation(models.Model):
    restro = models.ForeignKey(Restro, related_name='restro_under', on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, related_name='customer_under', on_delete=models.CASCADE)

    otp=models.IntegerField()

    date=models.DateField()
    time=models.TimeField()

    complete=models.BooleanField(default=False)

