from django.contrib import admin
from .models import Valet
# Register your models here.
class ValetAdmin(admin.ModelAdmin):
    list_display = ('id','user','zipcode','work_hr')

admin.site.register(Valet,ValetAdmin)
# Register your models here.
