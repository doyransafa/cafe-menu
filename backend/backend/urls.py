from django.contrib import admin
from django.urls import path, include
from restaurant.views import ProductViewSet, SubCategoryViewSet, CategoryViewSet, OrderViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'subcategories', SubCategoryViewSet, basename='subcategory')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
]

urlpatterns += router.urls
