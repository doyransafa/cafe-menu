from django.contrib import admin
from .models import Category, SubCategory, Product, VariantItem, VariantGroup

admin.site.register([Category, SubCategory, Product, VariantItem, VariantGroup])