from .models import Product, SubCategory, Category
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
  url = serializers.HyperlinkedIdentityField(view_name='category-detail', read_only=True)
  class Meta:
    model = Category
    fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):
  url = serializers.HyperlinkedIdentityField(view_name='subcategory-detail', read_only=True)
  main_category = CategorySerializer(read_only=True)
  class Meta:
    model = SubCategory
    fields = ['id', 'url', 'name', 'main_category']


class ProductSerializer(serializers.ModelSerializer):
  url = serializers.HyperlinkedIdentityField(view_name='product-detail', read_only=True)
  sub_category = SubCategorySerializer(read_only=True)

  class Meta:
    model = Product
    fields = ['id', 'url', 'name', 'description', 'price', 'sub_category']
