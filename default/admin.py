from django.contrib import admin
from .models import *
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('adress','number')

class EmailAdmin(admin.ModelAdmin):
    list_display = ('email',)

class FourTitleAdmin(admin.ModelAdmin):
    list_display = ('titleone','titletwo','titlethree','titlefour')

admin.site.register(Contact,ContactAdmin)
admin.site.register(Email,EmailAdmin)
admin.site.register(FourTitle,FourTitleAdmin)