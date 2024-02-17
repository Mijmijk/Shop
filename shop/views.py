from django.shortcuts import render, redirect
from .models import Product, Order


def catalog(request):
	products = Product.objects.all()
	return render(request,"shop/catalog.html", {'all_products': products})


def orders(request):
	orders_ = Order.objects.all()
	return render(request,"shop/orders.html", {'all_orders': orders_})


def create_order(request, id):
	product = Product.objects.get(id=id)
	if request.method == 'POST':
		Order.objects.create(
			product = product,
			delivery_address = request.POST['delivery_address']
		)
		return redirect('orders')
	return render(request,"shop/create_order.html", {'product': product})


def product_detail(request, id):
	product = Product.objects.get(id=id)
	return render(request,"shop/product_detail.html", {'product': product})
