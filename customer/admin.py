from django.contrib import admin
from .models import Customer,Order, Reservation
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id','user','zipcode')
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer','restro')
class ReserveAdmin(admin.ModelAdmin):
    list_display = ('customer','restro')

admin.site.register(Customer,CustomerAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(Reservation,ReserveAdmin)