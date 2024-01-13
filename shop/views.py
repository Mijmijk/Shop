from django.shortcuts import render
from .models import Product

def catalog(request):
	products = Product.objects.all()
	return render(request,"shop/catalog.html", {'all_products': products})
def orders(request):
	return render(request,"shop/orders.html")
def create_order(request):
	return render(request,"shop/create_order.html")
