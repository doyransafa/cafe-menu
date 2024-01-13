from django.shortcuts import render, HttpResponse
from .models import Product, SubCategory, Category

from rest_framework import viewsets
from .serializers import ProductSerializer, SubCategorySerializer, CategorySerializer

# Create your views here.

def first_view(request):
  return HttpResponse('First')

class ProductViewSet(viewsets.ModelViewSet):

  queryset = Product.objects.all().order_by('name')
  serializer_class = ProductSerializer

class SubCategoryViewSet(viewsets.ModelViewSet):

  queryset = SubCategory.objects.all().order_by('name')
  serializer_class = SubCategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):

  queryset = Category.objects.all().order_by('name')
  serializer_class = CategorySerializer