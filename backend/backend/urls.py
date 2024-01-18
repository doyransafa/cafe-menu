from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from restaurant.views import ProductViewSet, SubCategoryViewSet, CategoryViewSet, OrderViewSet, TabViewSet, TableViewSet

from rest_framework import routers
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'subcategories', SubCategoryViewSet, basename='subcategory')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'orders', OrderViewSet, basename='order')
router.register(r'tabs', TabViewSet, basename='tab')
router.register(r'tables', TableViewSet, basename='table')
# router.register(r'order_items', OrderItemViewSet, basename='order_item')
# router.register(r'order_item_variants', OrderItemVariantViewSet, basename='order_item_variant')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('schema', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]

urlpatterns += router.urls

#To serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
