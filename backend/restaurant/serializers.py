from urllib import request
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
  products_url = serializers.SerializerMethodField()
  
  class Meta:
    model = SubCategory
    fields = ['id', 'url', 'name', 'products_url', 'main_category']

  def get_products_url(self, obj):
    request = self.context.get('request')
    if request:
      return request.build_absolute_uri(f'/products?sub_category={obj.id}')
    return None


class ProductSerializer(serializers.ModelSerializer):
  url = serializers.HyperlinkedIdentityField(view_name='product-detail', read_only=True)
  sub_category = SubCategorySerializer(read_only=True)

  class Meta:
    model = Product
    fields = ['id', 'url', 'name', 'description', 'price', 'sub_category']
