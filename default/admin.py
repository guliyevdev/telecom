from django.contrib import admin
from .models import *
# Register your models here.
class LinksAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }
    list_display = ('name',)
admin.site.register(Links,LinksAdmin)