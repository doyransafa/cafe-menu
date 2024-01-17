import qrcode
from io import BytesIO
from PIL import Image
import secrets

from django.db import models
from django.core.files import File

class Table(models.Model):
  table_number = models.PositiveIntegerField(primary_key=True)
  qr_code = models.ImageField(blank=True, upload_to='qr_codes')
  token = models.CharField(max_length=255, unique=True, blank=True,)

  def generate_qr_code(self):
    if not self.qr_code:
      qr_image = qrcode.make(f'http://www.localhost:8080/{self.table_number}/menu?token={self.token}')
      qr_offset = Image.new('RGB', (370, 370), 'white')
      qr_offset.paste(qr_image)
      file_name = f'table-{self.table_number}-qr.png'
      stream = BytesIO()
      qr_offset.save(stream, 'PNG')
      self.qr_code.save(file_name, File(stream), save=False)
      qr_offset.close()

  def generate_token(self):
    if not self.token:
      self.token = secrets.token_urlsafe(32)

  def save(self, *args, **kwargs):
    self.generate_qr_code()
    self.generate_token()
    super().save(*args, **kwargs)

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

class Tab(models.Model):
  table = models.ForeignKey(Table, on_delete=models.CASCADE)
  total_price = models.FloatField()
  is_active = models.BooleanField(default=False)
  opened_at = models.DateTimeField(auto_now_add=True)
  closed_at = models.DateTimeField(null=True, blank=True) 

class Order(models.Model):
  tab = models.ForeignKey(Tab, on_delete=models.CASCADE, related_name='orders', null=True) ### remove null condition. ###
  table = models.ForeignKey(Table, on_delete=models.CASCADE)
  total_price = models.FloatField()
  created_at = models.DateTimeField(auto_now_add=True)
  
class OrderItem(models.Model):  
  order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  quantity = models.PositiveSmallIntegerField(default=1)
  total_price = models.FloatField()

class OrderItemVariant(models.Model):
  order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE, related_name='order_item_variants')
  variant_group = models.ForeignKey(VariantGroup, on_delete=models.CASCADE)
  selected_variant = models.ForeignKey(VariantItem, on_delete=models.CASCADE)
