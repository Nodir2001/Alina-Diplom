from django.contrib import admin
from .models import Order
from .forms import OrderForm

class OrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'good','master', 'message', 'purchase_date', 'purchase_time']
    form = OrderForm
    list_filter = ['name', 'phone']
    search_fields = ['name', 'phone']


admin.site.register(Order, OrderAdmin)