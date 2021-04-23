from django.contrib import admin
from .models import Restro,Menu
# Register your models here.
class RestroAdmin(admin.ModelAdmin):
    list_display = ('id','user','zipcode')

class MenuAdmin(admin.ModelAdmin):
    list_display = ('restro','dish','price')

admin.site.register(Restro,RestroAdmin)
admin.site.register(Menu,MenuAdmin)
# Register your models here.
