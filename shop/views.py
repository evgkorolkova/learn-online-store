from django.shortcuts import render
from .models import Order
from .models import Category
from .models import Writer
from .models import Profile
from .models import Product 	
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
# Create your views here.

def product_list(request):
	products = Product.objects.filter(date_create__lte=timezone.now()).order_by('date_create')
	return render(request, 'shop/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/product_detail.html', {'product': product})

