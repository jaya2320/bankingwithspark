from django.contrib import admin
from .models import Customer,Transaction_history
# Register your models here.
admin.site.register(Customer)
admin.site.register(Transaction_history)