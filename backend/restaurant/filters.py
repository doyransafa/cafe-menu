from django_filters import rest_framework as filters
from .models import Product

class SubCategoryFilter(filters.FilterSet):
  sub_category = filters.NumberFilter(field_name='sub_category__id', lookup_expr='exact')

  class Meta:
    model = Product
    fields = ['sub_category']

