from django.contrib import admin
from .models import Customer
from django.contrib.admin import ModelAdmin
# Register your models here.

class customerShow(ModelAdmin):
    list_display = ('First_name','Last_name','Email','membership','birth_date')

admin.site.register(Customer,customerShow)