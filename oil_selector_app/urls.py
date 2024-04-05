from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('cars/', CarListAPIView.as_view(), name='car-list'),
    path('cars/makers/', CarMakeListAPIView.as_view(), name='car-maker-list'),
    path('cars/models/', CarModelListAPIView.as_view(), name='car-model-list'),
    path('cars/years/', CarYearListAPIView.as_view(), name='car-year-list'),
    path('recommended-products/', RecommendedProductForCarAPIView.as_view(), name='recommended-product-for-car'),

]
