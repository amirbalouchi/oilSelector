from rest_framework import serializers
from ..models.product import Category, Product, ProductVariant, RecommendedProduct
from .car import CarSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'is_active', 'created_at', 'priority']
        ordering = ['priority']

class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = ['id', 'sku', 'unit']
        ordering = ['sku']

class ProductSerializer(serializers.ModelSerializer):
    variants = ProductVariantSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'description', 'image', 'external_url', 'variants', 'created_at']
        ordering = ['name']

class RecommendedProductSerializer(serializers.ModelSerializer):
    car = CarSerializer()
    product = ProductSerializer()

    class Meta:
        model = RecommendedProduct
        fields = ['id', 'car', 'product', 'capacity', 'capacity_note', 'recommendation_note', 'created_at', 'updated_at']