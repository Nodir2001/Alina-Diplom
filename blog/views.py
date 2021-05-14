from django.shortcuts import render
from django.utils import timezone
from .models import Order
from django.shortcuts import render, get_object_or_404
from .forms import OrderForm 

def home_page(request):
    return render(request, 'blog/landing.html',)
 

def order(request):
    form = OrderForm()
    context = {'form' : form}

    return render(request, 'blog/order.html', context)


def orderNow(request):
    form = OrderForm()
    context = {'form' : form}

    return render(request, 'blog/base.html', context)    