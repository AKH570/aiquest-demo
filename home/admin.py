from django.contrib import admin
from . models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display= ['product_name','price','discount','description','prod_img']

admin.site.register(Product,ProductAdmin)