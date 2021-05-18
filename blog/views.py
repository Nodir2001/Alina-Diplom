from django.shortcuts import render
from django.utils import timezone
from .models import Order 
from .forms import OrderForm 

def home_page(request):
    form = OrderForm()
    context = {'form' : form}

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            sphere = form.save(commit=False)
            sphere.save()

    return render(request, 'blog/landing.html', context)
   # return render(request, 'blog/landing.html',)
 

def order(request):

    form = OrderForm()
    context = {'form' : form}

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            sphere = form.save(commit=False)
            sphere.save()

    return render(request, 'blog/order.html', context)

'''
def orderNow(request):
    form = OrderForm()
    context = {'form' : form}

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            sphere = form.save(commit=False)
            sphere.save()

    return render(request, 'blog/landing.html', context)   ''' 