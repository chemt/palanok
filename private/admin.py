from django.contrib import admin
from models import Order
from models import Platej

admin.site.register(Order, Order.Admin)
admin.site.register(Platej, Platej.Admin)