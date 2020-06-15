from django.contrib import admin

# Register your models here.
from .models import Product, Writer, Category

admin.site.register(Product)
admin.site.register(Writer),
admin.site.register(Category)

