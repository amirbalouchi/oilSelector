# oil_selector_app/urls.py

from django.urls import path
from .views import CategoryListAPIView, CarListAPIView, RecommendedProductForCarAPIView

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('cars/', CarListAPIView.as_view(), name='car-list'),
    path('recommended-products/', RecommendedProductForCarAPIView.as_view(), name='recommended-product-for-car'),

]
