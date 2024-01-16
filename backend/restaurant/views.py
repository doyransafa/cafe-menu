from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

from .models import Product, SubCategory, Category, Order
from .serializers import ProductSerializer, SubCategorySerializer, CategorySerializer, OrderSerializer
from .filters import SubCategoryFilter


class ProductViewSet(viewsets.ModelViewSet):

  queryset = Product.objects.all().order_by('name')
  serializer_class = ProductSerializer
  filterset_class = SubCategoryFilter
  filter_backends = [DjangoFilterBackend, filters.SearchFilter]
  search_fields = ['name', 'description']

  @method_decorator(cache_page(60 * 60 * 2))
  def dispatch(self, request, *args, **kwargs):
    return super().dispatch(request, *args, **kwargs)

class SubCategoryViewSet(viewsets.ModelViewSet):

  queryset = SubCategory.objects.all().order_by('name')
  serializer_class = SubCategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):

  queryset = Category.objects.all().order_by('name')
  serializer_class = CategorySerializer

class OrderViewSet(viewsets.ModelViewSet):

  queryset = Order.objects.all().order_by('-created_at')
  serializer_class = OrderSerializer