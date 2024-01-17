from .models import Product, SubCategory, Category, VariantItem, VariantGroup, Order, OrderItem, OrderItemVariant, Tab
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


class VariantItemSerializer(serializers.ModelSerializer):
  class Meta:
    model = VariantItem
    fields = ['id', 'name', 'extra_price']


class VariantGroupSerializer(serializers.ModelSerializer):
  variant_items = VariantItemSerializer(many=True, required=False)
  class Meta:
    model = VariantGroup
    fields = ['id', 'name', 'type', 'variant_items']


class ProductSerializer(serializers.ModelSerializer):
  url = serializers.HyperlinkedIdentityField(view_name='product-detail', read_only=True)
  sub_category = serializers.PrimaryKeyRelatedField(queryset=SubCategory.objects.all())
  variant_groups = VariantGroupSerializer(many=True, required=False)

  class Meta:
    model = Product
    fields = ['id', 'url', 'name', 'description', 'price', 'availability', 'sub_category', 'variant_groups']

  def to_representation(self, instance):
    representation = super().to_representation(instance)
    representation['variant_groups'] = VariantGroupSerializer(instance.variant_groups.all(), many=True).data
    return representation

  def create(self, validated_data):
    variant_groups_data = validated_data.pop('variant_groups', [])
    product = Product.objects.create(**validated_data)

    for variant_group_data in variant_groups_data:
      variant_items_data = variant_group_data.pop('variant_items', [])
      variant_group = VariantGroup.objects.create(product=product, **variant_group_data)

      for variant_item_data in variant_items_data:
        VariantItem.objects.create(variant_group=variant_group, **variant_item_data)
    
    return product
  
  def update(self, instance, validated_data):
    variant_groups_data = validated_data.pop('variant_groups', [])
    instance.name = validated_data.get('name', instance.name)
    instance.description = validated_data.get('description', instance.description)
    instance.price = validated_data.get('price', instance.price)
    instance.sub_category = validated_data.get('sub_category', instance.sub_category)
    instance.save()

    for variant_group_data in variant_groups_data:
      variant_items_data = variant_group_data.pop('variant_items', [])
      variant_group, created = VariantGroup.objects.get_or_create(product=instance, **variant_group_data)

      for variant_item_data in variant_items_data:
        VariantItem.objects.update_or_create(variant_group=variant_group, **variant_item_data)

    return instance

class OrderItemVariantSerializer(serializers.ModelSerializer):
  class Meta:
    model = OrderItemVariant
    fields = ['variant_group', 'selected_variant']

class OrderItemSerializer(serializers.ModelSerializer):
  variants = OrderItemVariantSerializer(many=True, required=False)
  
  class Meta:
    model = OrderItem
    fields = ['product', 'quantity', 'total_price', 'variants']

  def create(self, validated_data):
    variants_data = validated_data.pop('variants', [])
    order_item = OrderItem.objects.create(**validated_data)

    for variant_data in variants_data:
      OrderItemVariant.objects.create(order_item=order_item, **variant_data)
    
    return order_item

class OrderSerializer(serializers.ModelSerializer):
  items = OrderItemSerializer(many=True, required=False)
  tab_url = serializers.SerializerMethodField()

  class Meta:
    model = Order
    fields = ['tab_url', 'items', 'created_at', 'total_price', 'table']

  def create(self, validated_data):

    items_data = validated_data.pop('items', [])
    table_id = validated_data.get('table')
    existing_tab = Tab.objects.filter(table_id=table_id, is_active=True).first()
    
    if existing_tab:
      order = Order.objects.create(tab=existing_tab, **validated_data)
      existing_tab.total_price += order.total_price
      existing_tab.save()
    else:
      new_tab = Tab.objects.create(table_id=table_id, total_price=validated_data.get('total_price'), is_active=True)
      order = Order.objects.create(tab=new_tab, **validated_data)    

    for item_data in items_data:
      order_items_variants_data = item_data.pop('variants', [])
      order_item = OrderItem.objects.create(order=order, **item_data)

      for variant_data in order_items_variants_data:
        OrderItemVariant.objects.create(order_item=order_item, **variant_data)

    return order
  
  def to_representation(self, instance):
    representation = super().to_representation(instance)
    representation['order_items'] = OrderItemSerializer(instance.order_items.all(), many=True).data
    return representation
  
  def get_tab_url(self, obj):
    request = self.context.get('request')
    tab = obj.tab
    if request and tab:
      return request.build_absolute_uri(f'/tabs/{tab.id}')
    return None
  
class TabSerializer(serializers.ModelSerializer):
  orders = OrderSerializer(many=True, required=False)

  class Meta:
    model = Tab
    fields = ['table', 'total_price', 'is_active', 'opened_at', 'closed_at', 'orders']