from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()


    context = {'orders': orders, 'customers': customers,
    'total_orders': total_orders, 'total_orders': total_orders, 'delivered': delivered, 'pending': pending
    }    
    return render(request, 'accounts/dashboard.html', context)



def products(request):
    products = Product.objects.all()

    return render(request, 'accounts/products.html', {'products': products})


def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)
    orders = customer.order_set.all()
    orders_count = orders.count()
    context = {'customer': customer, 'orders': orders, 'orders_count': orders_count}


    return render(request, 'accounts/customer.html', context)


def create_order(request):

    form = OrderForm()
    if request.method == 'POST':
        # print('Printing POST', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'accounts/order_form.html', context)


def update_order(request, pk):
    
    order = Order.objects.get(id=pk)    
    form = OrderForm(instance=order)

    if request.method == 'POST':
        # print('Printing POST', request.POST)
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'accounts/order_form.html', context)


def delete_order(request, pk):
    order = Order.objects.get(id=pk)
    context = {'item': order}
    if request.method == "POST":
        order.delete()
        return redirect('/')

    
    return render(request, 'accounts/delete.html', context)
