from django.contrib import admin

# Register your models here.
from .models import Product, Writer, Category, Profile

#admin.site.register(Product)
#admin.site.register(Writer),
#admin.site.register(Category)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'writer','url', 'sku', 'price', 'stock', 'status', 'writer_id', 'date_create')
    list_filter = ('price', 'status', 'writer_id', 'stock')
admin.site.register(Product, ProductAdmin)

@admin.register(Writer)
class WriterAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'url')

admin.site.register(Profile)
