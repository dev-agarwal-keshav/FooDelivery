from django.db import models
from django.contrib.auth.models import User


class Restro(models.Model):
    user=models.ForeignKey(User, related_name='restro', on_delete=models.CASCADE)

    name=models.CharField(max_length=300, default='')
    owner=models.CharField(max_length=300)
    phone=models.IntegerField()
    owner_phone = models.IntegerField()

    address=models.TextField()
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    zipcode=models.IntegerField()


class Menu(models.Model):
    restro=models.ForeignKey(User,related_name='menu_for_u',on_delete=models.CASCADE)

    dish=models.CharField(max_length=500)
    desc=models.TextField()
    photo=models.TextField()
    price=models.IntegerField()


class Tiffin_Menu(models.Model):
    restro = models.ForeignKey(User, related_name='tiffin', on_delete=models.CASCADE)

    m_bf=models.TextField()
    m_lun=models.TextField()
    m_din=models.TextField()

    tu_bf = models.TextField()
    tu_lun = models.TextField()
    tu_din = models.TextField()

    w_bf = models.TextField()
    w_lun = models.TextField()
    w_din = models.TextField()

    th_bf = models.TextField()
    th_lun = models.TextField()
    th_din = models.TextField()

    f_bf = models.TextField()
    f_lun = models.TextField()
    f_din = models.TextField()

    sa_bf = models.TextField()
    sa_lun = models.TextField()
    sa_din = models.TextField()

    s_bf = models.TextField()
    s_lun = models.TextField()
    s_din = models.TextField()