from django_filters import rest_framework as filters
from .models import Product, Tab

class SubCategoryFilter(filters.FilterSet):
  sub_category = filters.NumberFilter(field_name='sub_category__id', lookup_expr='exact')

  class Meta:
    model = Product
    fields = ['sub_category']

class ActiveTabFilter(filters.FilterSet):
  is_active = filters.BooleanFilter(field_name='is_active', lookup_expr='exact')

  class Meta:
    model = Tab
    fields = ['is_active']