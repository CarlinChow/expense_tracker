from django.contrib import admin
from .models import Transaction, Category, Transaction_Category

admin.site.register(Transaction)
admin.site.register(Category)
admin.site.register(Transaction_Category)