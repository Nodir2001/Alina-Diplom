from django.contrib import admin
from .models import Order
from .forms import OrderForm

class OrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'good','master', 'message', 'purchase_date']
    form = OrderForm
    list_filter = ['name', 'phone', 'email', 'good','master', 'message', 'purchase_date']
    search_fields = ['name', 'phone', 'email', 'good','master', 'message', 'purchase_date']


admin.site.register(Order, OrderAdmin)