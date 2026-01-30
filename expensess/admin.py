from django.contrib import admin
from .models import Category, Expense

admin.site.register(Category)  # expenses registered in admin
admin.site.register(Expense)
