from django.contrib import admin
from .models import Category, SubCategory, Product, VariantItem, VariantGroup, Table, Order, OrderItem, OrderItemVariant, Tab

admin.site.register([Category, SubCategory, Product, VariantItem, VariantGroup, Table, Order, OrderItem, OrderItemVariant, Tab])