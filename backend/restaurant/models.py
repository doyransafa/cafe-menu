from django.db import models

class Table(models.Model):
  table_number = models.PositiveIntegerField(primary_key=True)

  def __str__(self) -> str:
    return f'Table {self.table_number}'
  
class Category(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self) -> str:
    return f'Category: {self.name}'
  
class SubCategory(models.Model):
  name = models.CharField(max_length=100)
  main_category = models.ForeignKey(Category, on_delete=models.CASCADE)

  def __str__(self) -> str:
    return f'SubCategory: {self.main_category.name} > {self.name}'

class Product(models.Model):
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=1000)
  price = models.FloatField()
  availability = models.BooleanField(default=True)
  sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

  def __str__(self) -> str:
    return f'Product: {self.name}'

class VariantGroup(models.Model):
  name = models.CharField(max_length=100)
  type = models.CharField(max_length=50) # Radio, Checkbox
  product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variant_groups')

  def __str__(self) -> str:
    return f'Variant Group for {self.product.name} - {self.name}'

class VariantItem(models.Model):
  name = models.CharField(max_length=100)
  extra_price = models.FloatField()
  variant_group = models.ForeignKey(VariantGroup, on_delete=models.CASCADE, related_name='variant_items')

  def __str__(self) -> str:
    return f'Variant Item for {self.variant_group.name} - {self.name}'

class Order(models.Model):
  # table = models.ForeignKey(Table, on_delete=models.CASCADE)
  total_price = models.FloatField()
  created_at = models.DateTimeField(auto_now_add=True)
  
class OrderItem(models.Model):  
  order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  quantity = models.PositiveSmallIntegerField(default=1)
  total_price = models.FloatField()

class OrderItemVariant(models.Model):
  order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
  variant_group = models.ForeignKey(VariantGroup, on_delete=models.CASCADE)
  selected_variant = models.ForeignKey(VariantItem, on_delete=models.CASCADE)

