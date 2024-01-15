from re import search
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Product, SubCategory, Category
from .serializers import ProductSerializer, SubCategorySerializer, CategorySerializer
from .filters import SubCategoryFilter

# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):

  queryset = Product.objects.all().order_by('name')
  serializer_class = ProductSerializer
  filterset_class = SubCategoryFilter
  filter_backends = [DjangoFilterBackend, filters.SearchFilter]
  search_fields = ['name', 'description']

class SubCategoryViewSet(viewsets.ModelViewSet):

  queryset = SubCategory.objects.all().order_by('name')
  serializer_class = SubCategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):

  queryset = Category.objects.all().order_by('name')
  serializer_class = CategorySerializer